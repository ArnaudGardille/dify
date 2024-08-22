from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage
import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .google_auth_utils import authenticate_google_api

class GoogleCalendarEventsTool(BuiltinTool):

    def _invoke(self, user_id, tool_parameters):
        try:
            # Authenticate using the common utility function
            creds = authenticate_google_api(self.runtime.credentials)
            service = build("calendar", "v3", credentials=creds)

            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
            print("Getting the upcoming 10 events")
            events_result = (
                service.events()
                .list(
                    calendarId="primary",
                    timeMin=now,
                    maxResults=10,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )
            events = events_result.get("items", [])

            if not events:
                return self.create_text_message(text="No upcoming events found.")

            # Collect event details
            event_list = []
            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                event_list.append({"start": start, "summary": event["summary"]})

            return self.create_json_message({"events": event_list})

        except HttpError as error:
            return self.create_text_message(text=f"An error occurred: {error}")
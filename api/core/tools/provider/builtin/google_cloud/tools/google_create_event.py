from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .google_auth_utils import authenticate_google_api
import json

class GoogleCreateEventTool(BuiltinTool):

    def _invoke(self, user_id, tool_parameters):
        summary = tool_parameters.get('summary')
        location = tool_parameters.get('location')
        description = tool_parameters.get('description')
        start_datetime = tool_parameters.get('start_datetime')
        end_datetime = tool_parameters.get('end_datetime')
        timezone = tool_parameters.get('timezone', 'UTC')
        attendees_emails = tool_parameters.get('attendees_emails', '')
        recurrence = tool_parameters.get('recurrence', '')
        reminders = tool_parameters.get('reminders', '')

        # Parse comma-separated strings into lists or JSON objects as necessary
        attendees = [{'email': email.strip()} for email in attendees_emails.split(',') if email.strip()]
        recurrence_list = [rule.strip() for rule in recurrence.split(',') if rule.strip()]
        reminders_json = json.loads(reminders) if reminders else {'useDefault': False, 'overrides': []}

        try:
            # Authenticate using the common utility function
            creds = authenticate_google_api(self.runtime.credentials)
            service = build("calendar", "v3", credentials=creds)

            # Prepare the event details
            event = {
                'summary': summary,
                'location': location,
                'description': description,
                'start': {
                    'dateTime': start_datetime,
                    'timeZone': timezone,
                },
                'end': {
                    'dateTime': end_datetime,
                    'timeZone': timezone,
                },
                'recurrence': recurrence_list,
                'attendees': attendees,
                'reminders': reminders_json,
            }

            # Insert the event into the primary calendar
            event_result = service.events().insert(calendarId='primary', body=event).execute()
            
            return self.create_text_message(text=f"Event created: {event_result.get('htmlLink')}")

        except HttpError as error:
            return self.create_text_message(text=f"An error occurred: {error}")
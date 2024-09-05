from core.tools.tool.builtin_tool import BuiltinTool
import requests, json, uuid

class RemoveCalendarEventTool(BuiltinTool):

    def _invoke(self, user_id, tool_parameters):
        token = tool_parameters['token']
        calendar_event_id = tool_parameters['calendar_event_id']

        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "calendar.event.Remove",
                "api_version": "1.2",
                "app_token": credentials['wimi_api_key'],
                "msg_key": f"calendar.event.Remove.{str(uuid.uuid4())}",  # Unique message key
                "token": token,
                "identification": {
                    "account_id": int(credentials['wimi_account_id']),
                    "user_id": int(credentials['wimi_user_id']),
                    "project_id": int(tool_parameters['project_id']),
                    "calendar_event_id": calendar_event_id
                }
            },
            "body": {
                "data": {}
            }
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post("https://api.wimi.pro", headers=headers, data=json.dumps(payload))
        
        if response.status_code != 200 or 'error' in response.json().get('body', {}):
            return self.create_text_message(text="Failed to remove calendar event.\n\n" + response.text)
        
        return self.create_text_message(text=f"Calendar event '{calendar_event_id}' removed successfully.")
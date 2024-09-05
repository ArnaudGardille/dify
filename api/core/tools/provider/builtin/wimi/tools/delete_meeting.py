from core.tools.tool.builtin_tool import BuiltinTool
import requests, json, uuid

class DeleteMeetingTool(BuiltinTool):

    def _invoke(self, user_id, tool_parameters):
        token = tool_parameters['token']
        meeting_id = tool_parameters['meeting_id']

        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "meeting.meeting.Delete",
                "api_version": "1.2",
                "app_token": credentials['wimi_api_key'],
                "msg_key": f"meeting.meeting.Delete.{str(uuid.uuid4())}",  # Unique message key
                "token": token,
                "identification": {
                    "account_id": int(credentials['wimi_account_id']),
                    "user_id": int(credentials['wimi_user_id']),
                    "project_id": int(tool_parameters['project_id']),
                    "meeting_id": meeting_id
                }
            },
            "body": {
                "data": {}
            }
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post("https://api.wimi.pro", headers=headers, data=json.dumps(payload))
        
        if response.status_code != 200 or 'error' in response.json().get('body', {}):
            return self.create_text_message(text="Failed to delete meeting.\n\n" + response.text)
        
        return self.create_text_message(text=f"Meeting '{meeting_id}' deleted successfully.")
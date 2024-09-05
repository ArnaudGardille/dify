from core.tools.tool.builtin_tool import BuiltinTool
import requests, json, uuid

class GetMeetingListTool(BuiltinTool):

    def _invoke(self, user_id, tool_parameters):
        token = tool_parameters['token']

        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "meeting.meeting.GetList",
                "api_version": "1.2",
                "app_token": credentials['wimi_api_key'],
                "msg_key": f"meeting.meeting.GetList.{str(uuid.uuid4())}",  # Unique message key
                "token": token,
                "identification": {
                    "account_id": int(credentials['wimi_account_id']),
                    "user_id": int(credentials['wimi_user_id']),
                    "project_id": int(tool_parameters['project_id'])
                }
            },
            "body": {
                "data": {}
            }
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post("https://api.wimi.pro", headers=headers, data=json.dumps(payload))
        
        if response.status_code != 200 or 'error' in response.json().get('body', {}):
            return self.create_text_message(text="Failed to retrieve meeting list.\n\n" + response.text)
        
        meetings = response.json().get('body', {}).get('data', {}).get('meetings', [])
        return [self.create_json_message(meeting) for meeting in meetings]
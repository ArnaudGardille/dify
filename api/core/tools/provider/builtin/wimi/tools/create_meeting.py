from core.tools.tool.builtin_tool import BuiltinTool
import requests, json, uuid

class AddMeetingTool(BuiltinTool):

    def _invoke(self, user_id, tool_parameters):
        token = tool_parameters['token']
        name = tool_parameters['name']
        place = tool_parameters['place']
        description = tool_parameters.get('description', '')
        dates = tool_parameters['dates']
        user_id_list = str(tool_parameters.get('user_id_list', "[]"))
        ext_user_list = str(tool_parameters.get('ext_user_list', "[]"))
        notify_availability = tool_parameters.get('notify_availability', True)
        notify_creation = tool_parameters.get('notify_creation', True)

        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "meeting.meeting.Add",
                "api_version": "1.2",
                "app_token": credentials['wimi_api_key'],
                "msg_key": f"meeting.meeting.Add.{str(uuid.uuid4())}",  # Unique message key
                "token": token,
                "identification": {
                    "account_id": int(credentials['wimi_account_id']),
                    "user_id": int(credentials['wimi_user_id']),
                    "project_id": int(tool_parameters['project_id'])
                }
            },
            "body": {
                "data": {
                    "user_id_list": user_id_list,
                    "ext_user_list": ext_user_list,
                    "name": name,
                    "place": place,
                    "description": description,
                    "dates": dates,
                    "notify_availability": notify_availability,
                    "notify_creation": notify_creation,
                }
            }
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post("https://api.wimi.pro", headers=headers, data=json.dumps(payload))
        
        if response.status_code != 200 or 'error' in response.json().get('body', {}):
            return self.create_text_message(text="Failed to add meeting.\n\n" + response.text)
        
        return self.create_text_message(text=f"Meeting '{name}' added successfully.")
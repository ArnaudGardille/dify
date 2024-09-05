from core.tools.tool.builtin_tool import BuiltinTool
import requests, json, time

class GetChatListTool(BuiltinTool):

    def _invoke(self, user_id, tool_parameters):
        token = tool_parameters['token']

        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "chat.chat.GetList",
                "api_version": "1.2",
                "app_token": credentials['wimi_api_key'],
                "msg_key": f"chat.chat.GetList.{int(time.time())}",
                "token": token,
                "identification": {
                    "account_id": int(credentials['wimi_account_id']),
                    "user_id": int(credentials['wimi_user_id'])
                }
            },
            "body": {
                "data": {
                    "comment_count": True,
                    "offset": 0,
                    "limit": 1000,
                    "chat": True,
                    "channel": True
                }
            }
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post("https://api.wimi.pro", headers=headers, data=json.dumps(payload))
        
        if response.status_code != 200 or 'error' in response.json().get('body', {}):
            return self.create_text_message(text="Failed to retrieve chat list.\n\n" + response.text)
        
        chats = response.json().get('body', {}).get('data', {}).get('chats', [])
        return [self.create_json_message(chat) for chat in chats]
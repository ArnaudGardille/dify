from core.tools.tool.builtin_tool import BuiltinTool
import requests, json, time

class PostChatMessageTool(BuiltinTool):
    
    def _invoke(self, user_id, tool_parameters):
        message = tool_parameters['message']
        token = tool_parameters['token']
        chat_id = tool_parameters['chat_id']

        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "chat.chat.PostMessage",
                "api_version": "1.2",
                "app_token": credentials['wimi_api_key'],
                "msg_key": f"chat.chat.PostMessage.{int(time.time())}",
                "token": token,
                "identification": {
                    "account_id": int(credentials['wimi_account_id']),
                    "user_id": int(credentials['wimi_user_id']),
                    "chat_id": chat_id
                }
            },
            "body": {
                "data": {
                    "message": message,
                    "integration_attachment": None
                }
            }
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post("https://api.wimi.pro", headers=headers, data=json.dumps(payload))
        
        if response.status_code != 200 or 'error' in response.json().get('body', {}):
            return self.create_text_message(text="Failed to post message.\n\n" + response.text)
        
        return self.create_text_message(text=f"Message posted successfully.")
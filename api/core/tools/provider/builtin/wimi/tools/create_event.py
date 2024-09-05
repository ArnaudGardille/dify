from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage
import requests, json, uuid

class CreateEventTool(BuiltinTool):
    def _invoke(self, user_id, tool_parameters):
        title = tool_parameters['title']
        start_date = tool_parameters['start_date']
        end_date = tool_parameters['end_date']
        description = tool_parameters.get('description', '')

        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "calendar.event.Create",
                "api_version": "1.2",
                "app_token": credentials['wimi_api_key'],
                "msg_key": f"calendar.event.Create.{str(uuid.uuid4())}",  # Unique message key
                "token": tool_parameters['token'],
                "identification": {
                    "account_id": int(credentials['wimi_account_id']),
                    "user_id": int(credentials['wimi_user_id']),
                    "project_id": int(tool_parameters['project_id']),
                }
            },
            "body": {
                "data": {
                    "title": title,
                    "start_date": start_date,
                    "end_date": end_date,
                    "description": description,
                    "location": "",
                    "all_day": False,
                    "users": [],
                    "timezone": "Europe/Paris",
                    "is_public": True
                }
            }
        }
        
        headers = {'Content-Type': 'application/json'}
        response = requests.post(credentials['wimi_api_url'], headers=headers, data=json.dumps(payload))
        
        if 'error' in response.json()['body']:
            return self.create_text_message(text=response.text+'\n\n'+str(payload))
            
        return self.create_text_message(text=f"Event '{title}' created successfully.")

        
        
        
        return self.create_json_message({"token": token, "project_id": project_id})
        
        if response.status_code == 200:
            return self.create_text_message(text=f"Event '{title}' created successfully.")
        else:
            return self.create_text_message(text=f"Failed to create event '{title}'. Error: {response.text}")

from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage
import requests, json, uuid

def get_project_id_by_name(list_projects, project_name):
    for project in list_projects:
        if project['name'] == project_name:
            return project['project_id']
    return None

class CreateEventTool(BuiltinTool):
    def _invoke(self, user_id, tool_parameters):
        title = tool_parameters['title']
        date_time = tool_parameters['date_time']
        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "calendar.event.Create",
                "app_token": credentials['wimi_api_key'],
                "msg_key": f"calendar.event.Create.{str(uuid.uuid4())}",  # Unique message key
                "token": credentials['token'],
                "identification": {
                    "account_id": credentials['wimi_account_id'],
                    "user_id": credentials['wimi_user_id'],
                    "project_id": credentials['token'],
                }
            },
            "body": {
                "data": {
                    "title": title,
                    "date_time": date_time,
                }
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(credentials['wimi_api_url'], headers=headers, data=json.dumps(payload))
        print(response.json())
        
        if response.status_code == 200:
            return self.create_text_message(text=f"Event '{title}' created successfully.")
        else:
            return self.create_text_message(text=f"Failed to create event '{title}'. Error: {response.text}")
        
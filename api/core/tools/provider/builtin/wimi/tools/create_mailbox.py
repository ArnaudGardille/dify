from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage
import requests, json, uuid

def get_project_id_by_name(list_projects, project_name):
    for project in list_projects:
        if project['name'] == project_name:
            return project['project_id']
    return None

class CreateMailboxTool(BuiltinTool):
    def _invoke(self, user_id, tool_parameters):
        email = tool_parameters['email']
        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "mail.mailbox.CreateMailbox",
                "app_token": credentials['wimi_api_key'],
                "token": credentials['token'],
                "identification": {
                    "account_id": credentials['wimi_account_id'],
                    "user_id": credentials['wimi_user_id']
                }
            },
            "body": {
                "data": {
                    "email": email,
                    "project_id": credentials['project_id'],
                }
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(credentials['wimi_api_url'], headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            return self.create_text_message(text=f"Mailbox {email} created successfully.")
        else:
            return self.create_text_message(text=f"Failed to create mailbox {email}. Error: {response.text}")
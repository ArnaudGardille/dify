from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage
import requests, json, uuid
from pprint import pprint
import json

def get_project_id_by_name(list_projects, project_name):
    for project in list_projects:
        if project['name'] == project_name:
            return project['project_id']
    return None

class AuthenticateTool(BuiltinTool):
    def _invoke(self, user_id, tool_parameters):
        credentials = self.runtime.credentials
        payload = {
            "header": {
                "app_token": credentials['wimi_api_key'],
                "api_version": "1.2",
                "msg_key": f"auth.user.login.{str(uuid.uuid4())}",
                "identification": {
                    "account_id": credentials['wimi_account_id'],
                },
                "target": "auth.user.login",
                "auth": {
                    "login": credentials['wimi_login'],
                    "password": credentials['wimi_password']
                }
            },
            "body": {
                "data": {
                    "token": None,
                    "list_projects": True,
                    "projects_auth": True,
                    "projects_stats": True,
                    "projects_tasks_stats": True,
                    "projects_users": True,
                    "manual": True,
                    "csrf_security": True,
                    "fetch_pwd_sha": True,
                }
            }
        }
        pprint(payload)

        headers = {'Content-Type': 'application/json'}
        response = requests.post(credentials['wimi_api_url'], headers=headers, data=json.dumps(payload))

        if response.status_code != 200 or 'body' not in response.json():
            raise Exception("Authentication failed.")
        print(response.json())
        auth_response = response.json()
        token = auth_response['header']['token']
        project_id = get_project_id_by_name(auth_response['body']['data']['projects'], credentials['wimi_project_name'])
        print("Authentication succeeded.")
        
        return self.create_json_message({"token": token, "project_id": project_id})
from core.tools.tool.builtin_tool import BuiltinTool
import requests, json, uuid

class GetAllTasksTool(BuiltinTool):

    def _invoke(self, user_id, tool_parameters):
        token = tool_parameters['token']
        task_list_id = tool_parameters['task_list_id']

        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "task.task.GetAll",
                "api_version": "1.2",
                "app_token": credentials['wimi_api_key'],
                "msg_key": f"task.task.GetAll.{str(uuid.uuid4())}",  # Unique message key
                "token": token,
                "identification": {
                    "account_id": int(credentials['wimi_account_id']),
                    "user_id": int(credentials['wimi_user_id']),
                    "project_id": int(tool_parameters['project_id']),
                    "task_list_id": task_list_id
                }
            },
            "body": {
                "data": {}
            }
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post("https://api.wimi.pro", headers=headers, data=json.dumps(payload))
        
        if response.status_code != 200 or 'error' in response.json().get('body', {}):
            return self.create_text_message(text="Failed to retrieve tasks.\n\n" + response.text)
        
        tasks = response.json().get('body', {}).get('data', {}).get('tasks', [])
        return [self.create_json_message(task) for task in tasks]
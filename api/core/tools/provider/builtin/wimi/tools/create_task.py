from core.tools.tool.builtin_tool import BuiltinTool
import requests, json, uuid

class CreateTaskTool(BuiltinTool):

    def _invoke(self, user_id, tool_parameters):
        token = tool_parameters['token']
        label = tool_parameters['label']
        description = tool_parameters.get('description', '')
        position = tool_parameters.get('position', 0)
        status = tool_parameters.get('status', 0)
        due_date = tool_parameters.get('due_date', None)
        owners = str(tool_parameters.get('owners', "[]"))
        force_owners = tool_parameters.get('force_owners', False)

        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "task.task.Create",
                "api_version": "1.2",
                "app_token": credentials['wimi_api_key'],
                "msg_key": f"task.task.Create.{str(uuid.uuid4())}",  # Unique message key
                "token": token,
                "identification": {
                    "account_id": int(credentials['wimi_account_id']),
                    "user_id": int(credentials['wimi_user_id']),
                    "project_id": int(tool_parameters['project_id']),
                    "task_list_id": int(tool_parameters['task_list_id'])
                }
            },
            "body": {
                "data": {
                    "label": label,
                    "description": description,
                    "position": position,
                    "status": status,
                    "due_date": due_date,
                    "owners": owners,
                    "forceOwners": force_owners,
                }
            }
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post("https://api.wimi.pro", headers=headers, data=json.dumps(payload))
        
        if response.status_code != 200 or 'error' in response.json().get('body', {}):
            return self.create_text_message(text="Failed to create task.\n\n" + response.text)
        
        return self.create_text_message(text=f"Task '{label}' created successfully.")
from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage
import requests, json, uuid
from pprint import pprint

def get_project_id_by_name(list_projects, project_name):
    print("list_projects", list_projects)
    for project in list_projects:
        if project['name'] == project_name:
            return project['project_id']
    return None

class GetEventListTool(BuiltinTool):

    def _invoke(self, user_id, tool_parameters):
        start_date = tool_parameters.get('start_date')
        end_date = tool_parameters.get('end_date')
        view_busy = tool_parameters.get('view_busy', True)
        view_empty_events = tool_parameters.get('view_empty_events', True)
        gen_rec_occurrences = tool_parameters.get('gen_rec_occurrences', True)
        modified_after = tool_parameters.get('modified_after', " 2000-01-01 00:00:00")

        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "calendar.event.GetList",
                'api_version': '1.2',
                "app_token": credentials['wimi_api_key'],
                "msg_key": f"calendar.event.GetList.{str(uuid.uuid4())}",  # Unique message key
                "token": credentials['token'],
                "identification": {
                    "account_id": credentials['wimi_account_id'],
                    "user_id": credentials['wimi_user_id'],
                    "project_id": credentials['project_id'],
                },
            },
            "body": {
                "data": {
                    "start_date": start_date,
                    "end_date": end_date,
                    "view_busy": False,
                    "view_empty_events": True,
                    "gen_rec_occurrences": True,
                    "view_busy": view_busy,
                    "view_empty_events": view_empty_events,
                    "gen_rec_occurrences": gen_rec_occurrences,
                    "modified_after": modified_after
                }
            }
        }
        print("payload")
        pprint(payload)
        
        headers = {'Content-Type': 'application/json'}
        response = requests.post(credentials['wimi_api_url'], headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            pprint(response.json())
            events = response.json().get('body', {}).get('data', {}).get('events', [])
            print("events", events)
            return self.create_text_message(text=f"Retrieved {len(events)} events.")
        else:
            return self.create_text_message(text=f"Failed to retrieve events. Error: {response.text}")
from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage
import requests, json, uuid

class GetEventListTool(BuiltinTool):

    def _invoke(self, user_id, tool_parameters):
        start_date = tool_parameters.get('start_date')
        end_date = tool_parameters.get('end_date')
        view_busy = tool_parameters.get('view_busy', True)
        view_empty_events = tool_parameters.get('view_empty_events', True)
        gen_rec_occurrences = tool_parameters.get('gen_rec_occurrences', True)
        project_id = int(tool_parameters['project_id'])

        credentials = self.runtime.credentials

        payload = {
            "header": {
                "target": "calendar.event.GetList",
                'api_version': '1.2',
                "app_token": credentials['wimi_api_key'],
                "msg_key": f"calendar.event.GetList.{str(uuid.uuid4())}",  # Unique message key
                "token": tool_parameters['token'],
                "identification": {
                    "account_id": int(credentials['wimi_account_id']),
                    "user_id": int(credentials['wimi_user_id']),
                    "project_id": int(tool_parameters['project_id']),
                }
            },
            "body": {
                "data": {
                    "start_date": start_date,
                    "end_date": end_date,
                    "view_busy": view_busy,
                    "view_empty_events": view_empty_events,
                    "gen_rec_occurrences": gen_rec_occurrences,
                }
            }
        }
        
        headers = {'Content-Type': 'application/json'}
        response = requests.post(credentials['wimi_api_url'], headers=headers, data=json.dumps(payload))
        
        
        if 'error' in response.json()['body']:
            return self.create_text_message(text=response.text+'\n\n'+str(payload))
            
        return [self.create_json_message(event) for event in response.json()['body']['data']['events']]


        response.json().get('body', {}).get('data', {}).get('events', [])
        if response.status_code == 200:
            events = response.json().get('body', {}).get('data', {}).get('events', [])
            print("events", events)
            return self.create_text_message(text=f"Retrieved {len(events)} events.")
        else:
            return self.create_text_message(text=response.text+'\n\n'+str(payload))
            
            return self.create_text_message(text=f"Failed to retrieve events. Error: {response.text}")
        
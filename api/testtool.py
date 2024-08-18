from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage
import requests, json, uuid
from core.tools.provider.builtin.wimi.tools.get_events_list import GetEventListTool

credentials = {
    'wimi_api_key': '35C25592-6D78-0510-4DA4-C0D39C8D834D',
    'wimi_account_id': 381812,
    'wimi_user_id': 2318823,
    'wimi_login': 'arnaud.gardille@vigie.ai',
    'wimi_password': 'Dechiktorren92!',
    'wimi_api_url': 'https://api.wimi.pro',
    'wimi_project_name': 'General'
}

# Example parameters for retrieving event list
tool_parameters = {
    'start_date': '2024-01-01 00:00:00',
    'end_date': '2024-12-31 23:59:59',
    'filters': [],
    'view_busy': True,
    'busy_user_id_list': [],
    'view_empty_events': True,
    'calendar_event_id_list': [],
    'gen_rec_occurrences': True,
    'modified_after': 0
}

# Initialize the tool and run it
get_event_list_tool = GetEventListTool()
get_event_list_tool.runtime = type('Runtime', (object,), {'credentials': credentials})

result = get_event_list_tool._invoke(user_id='test_user', tool_parameters=tool_parameters)
print(result)
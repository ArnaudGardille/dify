from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage
import requests, json, uuid
from core.tools.provider.builtin.wimi.tools.create_event import CreateEventTool

credentials = {
    'wimi_api_key': '35C25592-6D78-0510-4DA4-C0D39C8D834D',
    'wimi_account_id': 381812,
    'wimi_user_id': 2318823,
    'wimi_login': 'arnaud.gardille@vigie.ai',
    'wimi_password': 'Dechiktorren92!',
    'wimi_api_url': 'https://api.wimi.pro',
    'wimi_project_name': 'General'
}

# Example parameters for creating an event
tool_parameters = {
    'title': 'Test Event',
    'date_time': '2023-12-31 23:59:59'
}

# Initialize the tool and run it
create_event_tool = CreateEventTool()
create_event_tool.runtime = type('Runtime', (object,), {'credentials': credentials})

result = create_event_tool._invoke(user_id='test_user', tool_parameters=tool_parameters)
print(result)
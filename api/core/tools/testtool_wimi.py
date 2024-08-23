from tool.builtin_tool import BuiltinTool
from entities.tool_entities import ToolInvokeMessage
import requests, json, uuid
from provider.builtin.wimi.tools.create_event import CreateEventTool
from provider.builtin.wimi.tools.get_events_list import GetEventListTool

# Example parameters for creating an event
tool_parameters = {
    'title': 'Test Event',
    'date_time': '2023-12-31 23:59:59'
}

# Initialize the tool and run it
create_event_tool = CreateEventTool()
create_event_tool.runtime = type('Runtime', (object,), {'credentials': credentials})

result = get_event_list_tool._invoke(user_id='test_user', tool_parameters=tool_parameters)
print(result)

result = create_event_tool._invoke(user_id='test_user', tool_parameters=tool_parameters)
print(result)
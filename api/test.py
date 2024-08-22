from core.tools.provider.builtin.wimi.tools.authenticate import AuthenticateTool
import os
from dotenv import load_dotenv
from datetime import datetime
from pprint import pprint

load_dotenv('wimi.env')
class MockRuntime:
    def __init__(self):
        self.credentials = {
            'wimi_api_url': os.getenv('WIMI_API_URL'),
            'wimi_account_id': os.getenv('WIMI_ACCOUNT_ID'),
            'wimi_login': os.getenv('WIMI_LOGIN'),
            'wimi_password': os.getenv('WIMI_PASSWORD'),
            'wimi_api_key': os.getenv('WIMI_API_KEY'),
            'wimi_project_name': os.getenv('WIMI_PROJECT_NAME')
        }

def test_authenticate_tool():
    # Set up the mock runtime with environment credentials
    runtime = MockRuntime()
    
    # Initialize the AuthenticateTool with the mock runtime
    authenticate_tool = AuthenticateTool()
    authenticate_tool.runtime = runtime
    
    # Invoke the tool with test parameters (user_id is not used in this example)
    result = authenticate_tool._invoke(user_id=None, tool_parameters={})
    
    print(result.type)
    print(type(result.message))
    print(result.message)
    # Print out the results for verification
    print("Token:", result.message["token"])
    print("Project ID:", result.message["project_id"])

if __name__ == "__main__":
    test_authenticate_tool()
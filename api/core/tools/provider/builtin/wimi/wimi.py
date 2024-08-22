from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController
from core.tools.errors import ToolProviderCredentialValidationError
import uuid
import json
import requests

class WimiProvider(BuiltinToolProviderController):
    
    def authenticate(self, credentials):
        payload = {
            "header": {
                "app_token": credentials['wimi_api_key'],
                "api_version": "1.2",
                "msg_key": f"auth.user.login.{str(uuid.uuid4())}",
                "identification": {
                    "account_id": credentials['wimi_account_id']
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
                    "fetch_pwd_sha": True
                }
            }
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post(credentials['wimi_api_url'], headers=headers, data=json.dumps(payload))

        if response.status_code != 200 or 'body' not in response.json():
            raise Exception("Authentication failed.")

        return response.json()['header']['token']

    def _validate_credentials(self, credentials):
        try:
            # Authenticate to validate credentials with Wimi API.
            self.authenticate(credentials)
                
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
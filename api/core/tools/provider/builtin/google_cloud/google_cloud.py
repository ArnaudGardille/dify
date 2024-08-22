from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController
from core.tools.errors import ToolProviderCredentialValidationError
import json

class GoogleCloudProvider(BuiltinToolProviderController):

    def _validate_credentials(self, credentials):
        try:
            # Validate the provided credentials by attempting to load them as JSON
            creds_json = json.loads(credentials['google_creds_json'])
            if 'installed' not in creds_json and 'web' not in creds_json:
                raise ToolProviderCredentialValidationError("Invalid OAuth2 credentials JSON format.")
        except (ValueError, KeyError) as e:
            raise ToolProviderCredentialValidationError(f"Invalid credentials format: {str(e)}")
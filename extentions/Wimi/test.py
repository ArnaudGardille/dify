import requests
import json
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

# Input your login, password, and app token
url = "https://api.wimi.pro"
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
app_token = os.getenv('API_KEY')

def authenticate_user(url, login, password, app_token, account_name=""):
    payload = {
        "header": {
            "target": "auth.user.Login",
            "api_version": "1.2",
            "app_token": app_token,
            "msg_key": str(uuid.uuid4())  # Generating a unique message key
        },
        "body": {
            "data": {
                "login": login,
                "password": password,
                "account_name": account_name
            }
        }
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("Status code:", response.status_code)
    print("Raw response text:", response.text)  # Log the raw response text for debugging
    try:
        response_json = response.json()
        print("Response JSON:", response_json)
        return response_json
    except json.JSONDecodeError:
        print("Failed to parse JSON response")
        return None



# Authenticate User
auth_response = authenticate_user(url, login, password, app_token)
print("Auth Response:", auth_response)

if auth_response and 'body' in auth_response and 'data' in auth_response['body']:
    token = auth_response['body']['data']['token']
    account_id = auth_response['body']['data']['user']['account_id']
    user_id = auth_response['body']['data']['user']['user_id']
    
    def get_account_info(url, token, app_token, account_id, user_id):
        payload = {
            "header": {
                "target": "main.account.Get",
                "api_version": "1.2",
                "app_token": app_token,
                "msg_key": str(uuid.uuid4()),  # Unique message key
                "token": token,
                "identification": {
                    "account_id": account_id,
                    "user_id": user_id
                }
            },
            "body": {
                "data": {}
            }
        }
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print("Account Info Response status:", response.status_code)
        print("Account Info Raw response text:", response.text)
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Failed to parse JSON response")
            return None

    def list_files_and_folders(url, token, app_token, account_id, user_id, project_id):
        payload = {
            "header": {
                "target": "document.entry.List",
                "api_version": "1.2",
                "app_token": app_token,
                "msg_key": str(uuid.uuid4()),  # Unique message key
                "token": token,
                "identification": {
                    "account_id": account_id,
                    "user_id": user_id,
                    "project_id": project_id,
                    "dir_id": 0  # Set based on your directory structure
                }
            },
            "body": {
                "data": {
                    "no_comment_count": True,
                    "process_thumbnail": True
                }
            }
        }
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print("List Files Response status:", response.status_code)
        print("List Files Raw response text:", response.text)
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Failed to parse JSON response")
            return None

    # Fetch Account Info to get Project ID
    account_info = get_account_info(url, token, app_token, account_id, user_id)
    
    if account_info and 'body' in account_info and 'data' in account_info['body']:
        print("Account Info:", account_info)
        
        # For simplicity, assuming the first project ID
        project_id = account_info['body']['data']['account']['projects'][0]['id']

        # List Files and Folders
        files_and_folders = list_files_and_folders(url, token, app_token, account_id, user_id, project_id)
        if files_and_folders:
            print("Files and Folders:", files_and_folders)
    else:
        print("Failed to retrieve account information.")
else:
    print("Authentication failed.")
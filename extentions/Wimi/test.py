import requests
import json
import uuid
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

# Input your login, password, and app token
url = "https://api.wimi.pro"
LOGIN = os.getenv('LOGIN')
print("LOGIN", LOGIN)
PASSWORD = os.getenv('PASSWORD')
print("PASSWORD", PASSWORD)
APP_TOKEN = os.getenv('API_KEY')
print("APP_TOKEN", APP_TOKEN)
ACCOUNT_ID = os.getenv('ACCOUNT_ID')
print("LOGIN", LOGIN)

# Add the account ID from the environment variables
def authenticate_user(url, login, password, app_token, account_id="", verbose=True):
    payload = {
        "header": {
            "app_token": app_token,
            "api_version": "1.2",
            "msg_key": "auth.user.login.P0Tgh93ddU58W0yruYXk", #f"auth.user.login.{str(uuid.uuid4())}",  # Generating a unique message key
            "identification": {
                "account_id": account_id
            },
            "target": "auth.user.login",
            "debug": {
            "indent_output": True
            },
            "auth": {
                "login": login,
                "password": password
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
        },
    }
    
    if verbose:
        print("Payload:")
        pprint(payload)
        print()
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if verbose:
        print("Raw response:\n", response.text)
    
    try:
        response_json = response.json()
        return response_json
    except json.JSONDecodeError:
        print("Failed to parse JSON response")
        return None
    
def get_projects(url, app_token, token, account_id, user_id, verbose=True):
    payload = {
        "header": {
            "target": "main.account.getprojects",
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
            "data": {
            "calc_document_size": True,
            "with_categories": True,
            "projects_auth": True,
            "projects_stats": True,
            "projects_tasks_stats": True,
            "projects_users": True,
            "all_projects": True,
            "for_drive_synchro": True,
            "include_archived": True
        }
        }
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("Projects Info:")
    pprint(response.json())
    try:
        return response.json()
    except json.JSONDecodeError:
        print("Failed to parse JSON response")
        return None

# Authenticate User
print("Authenticating User...")
auth_response = authenticate_user(url, LOGIN, PASSWORD, APP_TOKEN, ACCOUNT_ID)


if auth_response and 'body' in auth_response and 'data' in auth_response['body']:
    token = auth_response['header']['token']
    user_id = auth_response['body']['data']['user']['user_id']
    user_name = auth_response['body']['data']['user']['display_name']
    print("Authenticated as:", user_name)
    
    print("Fetching Projects...")
    projects_info = get_projects(url, APP_TOKEN, token, ACCOUNT_ID, user_id, verbose=True)
    
    def get_account_info(url, token, app_token, account_id, user_id):
        payload = {
            "header": {
                "target": "main.account.get",
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
        print("Account Info:")
        pprint(response.json())
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Failed to parse JSON response")
            return None

    def list_files_and_folders(url, token, app_token, account_id, user_id, project_id=None):
        payload = {
            "header": {
                "target": "document.entry.list",
                "api_version": "1.2",
                "app_token": app_token,
                "msg_key": str(uuid.uuid4()),  # Unique message key
                "token": token,
                "identification": {
                    "account_id": account_id,
                    "user_id": user_id,
                    "project_id": project_id,
                    #"dir_id": 0  # Set based on your directory structure
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
        print("List Files Raw response text:")
        pprint(response.json())
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Failed to parse JSON response")
            return None

    # Fetch Account Info to get Project ID
    print("Fetching Account Info...")
    account_info = get_account_info(url, token, APP_TOKEN, ACCOUNT_ID, user_id)
    
    if account_info and 'body' in account_info and 'data' in account_info['body']:
        print("Account Info:")
        pprint(account_info)
        
        # For simplicity, assuming the first project ID
        #project_id = account_info['body']['data']['projects'][0]['id']

        # List Files and Folders
        print("Listing Files and Folders...")
        files_and_folders = list_files_and_folders(url, token, APP_TOKEN, ACCOUNT_ID, user_id) #, project_id)
        if files_and_folders:
            print("Files and Folders:", files_and_folders)
    else:
        print("Failed to retrieve account information.")
else:
    print("Authentication failed.")
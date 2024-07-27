import os.path
import requests

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os
from io import BytesIO
import mimetypes

from googleapiclient.http import MediaIoBaseDownload

import requests
from langchain_google_community import GoogleDriveLoader
from io import BytesIO

# Configuration for Dify API
DIFY_API_URL = 'http://my.vigie.ai/v1'
DIFY_API_KEY = 'dataset-eWoK4OqxwncqWQfmPDpXcr9t'
KNOWLEDGE_NAME = 'Google Drive'

# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/drive.metadata.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/drive.file"
]

# --- Dify API Functions 

def get_or_create_knowledge(name):
    # Check if knowledge exists
    url = f"{DIFY_API_URL}/datasets"
    headers = {
        'Authorization': f'Bearer {DIFY_API_KEY}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        datasets = response.json().get('data', [])
        for dataset in datasets:
            if dataset['name'] == name:
                print(f"Found knowledge base: {name}")
                return dataset['id']
    
    # Create new knowledge base if it doesn't exist
    print(f"Creating new knowledge base: {name}")
    url = f"{DIFY_API_URL}/datasets"
    data = {
        "name": name
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code in [200, 201]:
        return response.json()['id']
    else:
        raise Exception(f"Failed to create knowledge base: {response.text}")

def get_existing_documents(knowledge_id):
    url = f"{DIFY_API_URL}/datasets/{knowledge_id}/documents"
    headers = {
        'Authorization': f'Bearer {DIFY_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return {doc['name']: doc['id'] for doc in response.json().get('data', [])}
    else:
        raise Exception(f"Failed to fetch existing documents: {response.text}")

def upload_document_to_dify(knowledge_id, name, content, mime_type):
    url = f"{DIFY_API_URL}/datasets/{knowledge_id}/document/create_by_file"  # Corrected endpoint
    headers = {
        'Authorization': f'Bearer {DIFY_API_KEY}'
    }

    files = {
        'file': (name, BytesIO(content), mime_type), 
        # Add required parameters according to the API docs
        'data': (None, '{"indexing_technique":"high_quality","process_rule":{"mode": "automatic"}}', 'application/json')
    }
    
    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 201:
        print(f'Successfully uploaded {name} to Dify')
    else:
        error_response = response.json()
        print(f'Failed to upload {name} to Dify: {error_response.get("message", response.text)}')

def update_document_in_dify(knowledge_id, document_id, name, content, is_binary=False):
    url = f"{DIFY_API_URL}/datasets/{knowledge_id}/documents/{document_id}/update_by_text"
    headers = {
        'Authorization': f'Bearer {DIFY_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    if is_binary:
        # Convert binary content to a string representation (e.g., base64 encoding)
        import base64
        content = base64.b64encode(content).decode('utf-8')
    
    data = {
        "name": name,
        "text": content,
        "process_rule": {
            "mode": "automatic"
        }
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f'Successfully updated {name} in Dify')
    else:
        print(f'Failed to update {name} in Dify: {response.text}')

# Mapping Google MimeTypes to export formats and corresponding Dify MimeTypes
MIME_TYPE_MAPPING = {
    'application/vnd.google-apps.document': ('text/plain', 'txt'), # Export as plain text and upload as txt
    'application/vnd.google-apps.spreadsheet': ('text/csv', 'csv'), # Export as CSV and upload as csv
    'application/vnd.google-apps.presentation': ('application/pdf', 'pdf') # Export as PDF and upload as pdf
}

def upload_or_update_document(service, knowledge_id, item, existing_documents):
    document_name_in_dify_format = item["name"]
    file_id = item['id']
    mime_type = item['mimeType']

    if mime_type in MIME_TYPE_MAPPING:
        export_mime_type, dify_mime_type = MIME_TYPE_MAPPING[mime_type]
        request = service.files().export_media(fileId=file_id, mimeType=export_mime_type)
        file_content = request.execute()
        
        if document_name_in_dify_format in existing_documents:
            update_document_in_dify(knowledge_id, existing_documents[document_name_in_dify_format], item["name"], file_content, True)
        else:
            upload_document_to_dify(knowledge_id, item["name"], file_content, dify_mime_type)
    else:
        # For supported binary files
        if mimetypes.guess_extension(mime_type) in ['.txt', '.markdown', '.md', '.pdf', '.html', '.htm', '.xlsx', '.xls', '.docx', '.csv']:
            request = service.files().get_media(fileId=file_id)
            file_content = request.execute()

            if document_name_in_dify_format in existing_documents:
                update_document_in_dify(knowledge_id, existing_documents[document_name_in_dify_format], item["name"], file_content, True)
            else:
                upload_document_to_dify(knowledge_id, item["name"], file_content, mime_type)
        else:
            print(f"Unsupported file type: {item['name']} ({mime_type})")


# Mapping Google MimeTypes to Dify MimeTypes (simplified)
MIME_TYPE_MAPPING = {
    'application/vnd.google-apps.document': 'text/plain',
    'application/vnd.google-apps.spreadsheet': 'text/csv',
    'application/vnd.google-apps.presentation': 'application/pdf'
}



# --- Main Logic ---

def main():
    # 1. Load Documents from Google Drive using Langchain
    loader = GoogleDriveLoader(
        folder_id="root",  # Or specify a different folder ID
        credentials_path="/Users/gardille/.credentials/credentials.json", 
        recursive=True 
    )
    items = loader.load()  # This will give you Langchain Documents

    # 2. Get or Create the Knowledge Base in Dify
    knowledge_id = get_or_create_knowledge(KNOWLEDGE_NAME)
    existing_documents = get_existing_documents(knowledge_id)
    
    # 3. Upload or Update Documents in Dify
    for doc in items:
        page_content = doc.page_content.encode("utf-8") # Convert text to bytes
        document_name_in_dify_format = doc.metadata["source"].split("/")[-1]  
        mime_type = MIME_TYPE_MAPPING.get(doc.metadata.get('mimeType'), None)  # Get Dify mime type if it exists

        if document_name_in_dify_format in existing_documents:
            update_document_in_dify(knowledge_id, existing_documents[document_name_in_dify_format], 
                                    doc.metadata["source"].split("/")[-1], page_content)
        else:
            if mime_type:  # For Google Docs, Sheets, Slides (convert to plain text)
                upload_document_to_dify(knowledge_id, document_name_in_dify_format, 
                                        page_content, mime_type)
            else:  # For other supported file types (no conversion)
                upload_document_to_dify(knowledge_id, document_name_in_dify_format,
                                        page_content, doc.metadata.get('mimeType', 'text/plain'))  


if __name__ == "__main__":
    main()

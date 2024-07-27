import json
import requests
import os


# Define the URL and headers
url = 'http://my.vigie.ai/v1/datasets/ef576515-ad95-4811-aaa9-d32e450faeb0/document/create_by_file'
headers = {
    'Authorization': os.getenv('VIGIE_KNOWLEDGE_API_SECRET')
}

# Define the data and files parameters
data = {
    "indexing_technique": "high_quality",
    "process_rule": {
        "rules": {
            "pre_processing_rules": [
                {"id": "remove_extra_spaces", "enabled": True},
                {"id": "remove_urls_emails", "enabled": True}
            ],
            "segmentation": {
                "separator": "###",
                "max_tokens": 500
            }
        },
        "mode": "custom"
    }
}

files = {
    'file': ('docker-compose.yaml.docx', open('/Users/gardille/Downloads/docker-compose.yaml.docx', 'rb'), 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'),
    'data': (None, json.dumps(data), 'application/json')
}

# Make the POST request
response = requests.post(url, headers=headers, files=files)

# Print the response from the server
print(response.text)
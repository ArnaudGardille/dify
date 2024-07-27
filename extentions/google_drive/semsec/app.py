from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import numpy as np
import faiss
import fitz  # PyMuPDF

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


folder_id = None  # Initialize folder_id as None
client = MistralClient(api_key="")  # Update with your Mistral API key


@app.post("/set_folder/")
async def set_folder(folder_id_input: str = Form(...)):
    global folder_id
    folder_id = folder_id_input
    return {"message": "Folder ID set successfully"}


@app.post("/query")
async def query_drive(request: QueryRequest):
    if not folder_id:
        raise HTTPException(status_code=400, detail="Folder ID not set")

    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    SERVICE_ACCOUNT_FILE = '/path/to/json/file.json'  # Update this path
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    # Function to list files in Google Drive folder
    def list_files_in_folder(service, folder_id):
        query = f"'{folder_id}' in parents and trashed=false"
        try:
            results = service.files().list(q=query, pageSize=10,
                                           fields="files(id, name)").execute()
            items = results.get('files', [])
            if not items:
                print(f"No files found in the folder with ID: {folder_id}")
            return items
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    # Function to extract text from a PDF file
    def extract_text_from_pdf(file_path):
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    # Retrieve documents from Google Drive
    files = list_files_in_folder(service, folder_id)
    if not files:
        raise ValueError(
            f"No files found or unable to access the folder with ID: {folder_id}")

    documents = []
    for file in files:
        file_id = file['id']
        file_name = file['name']

        print(f"Downloading file: {file_name} (ID: {file_id})")
        request = service.files().get_media(fileId=file_id)
        with open(file_name, 'wb') as fh:
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()

        # Extract the content of the file based on its type
        if file_name.endswith('.pdf'):
            text = extract_text_from_pdf(file_name)
        elif file_name.endswith('.txt'):
            with open(file_name, 'r', encoding='utf-8') as f:
                text = f.read()
        else:
            continue  # Skip unsupported file types

        documents.append(text)

    # Split text into chunks
    chunk_size = 2048
    chunks = [doc[i:i + chunk_size] for doc in documents for i in
              range(0, len(doc), chunk_size)]

    # Define a function to get text embedding using Mistral AI
    def get_text_embedding(input):
        embeddings_batch_response = client.embeddings(
            model="mistral-embed",
            input=input
        )
        return embeddings_batch_response.data[0].embedding

    # Create embeddings for each text chunk
    text_embeddings = np.array([get_text_embedding(chunk) for chunk in chunks])

    # Load into a vector database (FAISS)
    d = text_embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(text_embeddings)

    # Create embeddings for the question
    question = request.query
    question_embeddings = np.array([get_text_embedding(question)])

    # Retrieve similar chunks from the vector database
    D, I = index.search(question_embeddings, k=2)  # Retrieve top 2 similar chunks
    retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

    # Combine context and question in a prompt and generate response
    prompt = f"""
    Context information is below.
    ---------------------
    {' '.join(retrieved_chunks)}
    ---------------------
    Given the context information and not prior knowledge, answer the query.
    Query: {question}
    Answer:
    """

    def run_mistral(user_message, model="mistral-medium-latest"):
        messages = [
            ChatMessage(role="user", content=user_message)
        ]
        chat_response = client.chat(
            model=model,
            messages=messages
        )
        return chat_response.choices[0].message.content

    answer = run_mistral(prompt)
    return {"answer": answer}


@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)


if __name__ == "__main__":
    import threading
    import uvicorn

    def run_app():
        uvicorn.run(app, host="0.0.0.0", port=8000)

    thread = threading.Thread(target=run_app, args=(), daemon=True)
    thread.start()

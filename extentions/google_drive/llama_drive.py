from llama_index.readers.google import GoogleDocsReader, GoogleDriveReader

# Specify the document IDs you want to load
document_ids = ["<document_id>"]


loader = GoogleDriveReader()
def load_data(folder_id: str):
    docs = loader.load_data(folder_id=folder_id)
    for doc in docs:
        doc.id_ = doc.metadata["file_name"]
    return docs

print("loading data...")
docs = load_data(folder_id="root")
print("docs:", docs)


# Load data from Google Docs
documents = GoogleDocsReader().load_data(document_ids=document_ids)
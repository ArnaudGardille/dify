from langchain_google_community import GoogleDriveLoader
from langchain_community.document_loaders import UnstructuredFileIOLoader

loader = GoogleDriveLoader(
    folder_id="root",
    file_types=["document", "sheet"],
    credentials_path="/Users/gardille/.credentials/credentials.json",
    # Optional: configure whether to recursively fetch files from subfolders. Defaults to False.
    recursive=True,
)

docs = loader.load()

print(docs)
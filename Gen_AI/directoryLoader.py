from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader

loader = DirectoryLoader("D:\Summer PEP\Data Folder", glob="**/*.pdf", loader_cls=PyPDFLoader, show_progress=True)
# documents = loader.load() # output in one go
documents = loader.lazy_load() #one by one output

for idx, document in enumerate(documents, start=1):
    print(f"\nDocument {idx}")
    print("Content:\n", document.page_content)
print("Metadata:\n", document.metadata)
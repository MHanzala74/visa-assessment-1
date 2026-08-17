import os
from langchain_community.document_loaders import PyPDFDirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings  
from langchain_community.vectorstores import Chroma

DATA_DIR = "./data/visa_docs"
CHROMA_DB_DIR = "./data/chroma_db"

def get_embedding_function():
    return OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

def ingest_documents(pdf_path: str = None):
    if pdf_path:
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
    else:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        loader = PyPDFDirectoryLoader(DATA_DIR)
        documents = loader.load()

    if not documents:
        return {"status": "error", "message": "No documents found to process."}

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )
    chunks = text_splitter.split_documents(documents)

    embeddings = get_embedding_function()
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )
    
    return {
        "status": "success", 
        "chunks_processed": len(chunks),
        "db_path": CHROMA_DB_DIR
    }
import os
from langchain_chroma import Chroma
from services.rag.ingest import get_embedding_function, CHROMA_DB_DIR

def get_retriever(k: int = 4):
    if not os.path.exists(CHROMA_DB_DIR):
        raise FileNotFoundError("Vector Database directory does not exist. Run ingest process first.")

    embeddings = get_embedding_function()
    vector_store = Chroma(
        persist_directory=CHROMA_DB_DIR, 
        embedding_function=embeddings
    )
    
    return vector_store.as_retriever(search_kwargs={"k": k})
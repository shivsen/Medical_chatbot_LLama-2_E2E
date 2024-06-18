
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

def data_loader(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    document = loader.load()
    return document



def text_split(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 400, chunk_overlap = 20)
    chunks = text_splitter.split_documents(data)

    return chunks

def download_huggingface_embedding_model():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

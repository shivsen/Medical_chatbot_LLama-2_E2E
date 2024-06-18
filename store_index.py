from src.helper import data_loader,  text_split, download_huggingface_embedding_model
from pinecone import Pinecone
from dotenv import load_dotenv
import os


load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

extracted_data = data_loader("data/")

chunks = text_split(extracted_data)[:1000]

embeddings = download_huggingface_embedding_model()

pc = Pinecone(api_key = PINECONE_API_KEY)
Index = pc.Index("chatbot")

    # Initialize an empty list to store the results
def vectors()   : 
    Embed_data = []

        # Loop through the chunks and get the embeddings
    for index, chunk in enumerate(chunks):
    # Get the embedded vectors for the current chunk
        vectors = embeddings.embed_query(chunk.page_content)
            
        # Create a dictionary with the index and values
        result = {"id": str(index), "values": vectors, "metadata" : {"text" : chunk.page_content}}
            
        # Append the dictionary to the results list
        Embed_data.append(result)

    
    return Embed_data
    

Embed_data = vectors()
    

Index.upsert(vectors=Embed_data)



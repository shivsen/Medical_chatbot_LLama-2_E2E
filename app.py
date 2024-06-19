from flask import Flask, render_template, jsonify, request
from src.helper import download_huggingface_embedding_model
from pinecone import Pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import LLMChain
from dotenv import load_dotenv
from src.prompt import prompt
import os


app=Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key = PINECONE_API_KEY)
Index = pc.Index("chatbot")

embeddings = download_huggingface_embedding_model()

llm = CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin", model_type="llama",
                    config={"temperature" : 0.8})

@app.route("/")

def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    
    query = input

    result = Index.query(
        vector=embeddings.embed_query(query),
        top_k=3,
        include_metadata=True
    )

    final_results = [match.get("metadata") for match in result.get("matches")]

    chain = LLMChain(llm=llm, prompt=prompt)

    return str(chain.run({"question" : query, "context" : final_results}))

if __name__== '__main__':
    app.run(debug=True)





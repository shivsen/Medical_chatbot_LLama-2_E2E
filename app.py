from flask import Flask, render_template, jsonify, request
from src.helper import download_huggingface_embedding_model
from pinecone import Pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import LLMChain
from dotenv import load_dotenv
from src.prompt import prompt
import os
from langchain.chains import SimpleSequentialChain
from langchain.chat_models import ChatOpenAI



app=Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key = PINECONE_API_KEY)
Index = pc.Index("chatbot")

embeddings = download_huggingface_embedding_model()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")


query = "headache"

result = Index.query(
    vector=embeddings.embed_query(query),
    top_k=5,
    include_metadata=True
)

final_results = [match.get("metadata") for match in result.get("matches")]


chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run({"question" : query, "context" : final_results}))




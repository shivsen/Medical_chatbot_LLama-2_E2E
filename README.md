# Medical_chatbot_LLama-2_E2E
A Medical Chatbot Using Llama2 and Hugging Face which tells you about the medical conditions and its treatments.

Step 1 
install requirements.txt
pip install -r requirements.txt

step 2 download the model from the hugging face in your local directly
llama-2-7b-chat.ggmlv3.q4_0.bi

step 3 : run store_index.py
python store_index.py (this code upsert all the vectors in given pinecone index)
Note : here i am using only 1000 vectors only and for this i use sentence transformer which gives 384 dimensions of vectors

step 4 : run app.py
python app.py

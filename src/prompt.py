from langchain.prompts import PromptTemplate


prompt = PromptTemplate(input_variables=["context", "question"],
                        template='''As a Good model generate a proper answer with good prensentation.user will pass the question.

context : {context}
question : {question}

you have to read the data from the context and try to answer and if you dont know simply says i dont know.
answer : ''')

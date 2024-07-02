from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")



# used to generate a prompt, following a template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant"),
        ("user","Question:{question}")
    ]
)


st.title('Langchain Demo With LLAMA3 API') # title for the app
input_text=st.text_input("Enter Querry") # input field for the app


llm=Ollama(model="llama3") # defining our model
output_parser=StrOutputParser() 
chain=prompt|llm|output_parser 

'''
The chain is used to define the workflow.
In this example, when the chain is invoked, the input is passed into the prompt. The formed prompt is then passed into the llm. 
Then the output of that llm is passed through the output parser. 
If an element of the chain does not take an input, it is not included in the chain. 
'''

if input_text:
    st.write(chain.invoke({"question":input_text}))

# we display the output using the write method.
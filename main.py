import os
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Define the prompt template
template = "You are a helpful assistant. \
Please provide a summary for the following text: {text}"
prompt = PromptTemplate(
    input_variables=["text"],
    template=template
)

# Initialize the language model
llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.7)

# Create the chain
chain = prompt | llm | StrOutputParser()

# Provide input and run the chain
input_text = "\
Devbox is a command-line tool that lets you easily create isolated\
shells for development. You start by defining the list of \
packages required for your project, and Devbox creates an isolated, \
reproducible environment with those packages installed.\
"
response = chain.invoke(input_text)

print(response)

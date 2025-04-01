from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

from langserve import add_routes
from fastapi import FastAPI
import uvicorn

import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


system_template = "You are story teller and u tell the story in {language}"
human_template = "{text}"

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system' , system_template),
        ('human' , human_template )
    ]
)

llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro" , temperature = 0 , convert_system_message_to_human=True)
parser = StrOutputParser()

chain = prompt_template | llm | parser

app = FastAPI(
    title="My Story Teller",
    description=" my langchain created api ",
    version="1.0"
)

add_routes(
    app,
    chain,
    path='/chain'
)

if __name__=="__main__":
    uvicorn.run(app,host = "localhost" , port = 8000)
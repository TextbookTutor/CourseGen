from langchain_openai import ChatOpenAI

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from models import MCQQuestion, FRQQuestion, ProblemSet

import os
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"), server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("You successfully connected to MongoDB!")
except Exception as e:
    print(e)

LLM = ChatOpenAI(model="gpt-4o-mini").with_structured_output(ProblemSet)
PROMPT = "Please generate a problem set of {} problems which contain both MCQ and text questions from the following text:\n\n{}"

def generate_problems(text: str, num_problems: int) -> ProblemSet:
    return LLM(PROMPT.format(num_problems, text))

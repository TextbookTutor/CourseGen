from langchain_openai import ChatOpenAI

from models import ProblemSet

from dotenv import load_dotenv
load_dotenv()

LLM = ChatOpenAI(model="gpt-4o-mini").with_structured_output(ProblemSet)
PROMPT = "Please generate a problem set of {} MCQ questions and {} FRQ questions from the following text:\n\n{}"

def generate_problems(text: str, mcq_count: int, frq_count: int) -> ProblemSet:
    return LLM(PROMPT.format(mcq_count, frq_count, text))

from pydantic import BaseModel, Field

class MCQQuestion(BaseModel):
    question: str = Field(title="Question", description="The question to ask", example="What is the capital of France?")
    options: list[str] = Field(title="Options", description="The options to choose from", example=["Paris", "London", "Berlin", "Madrid"])
    answer: int = Field(title="Answer", description="The index of the correct answer", example=0)

class MCQSet(BaseModel):
    questions: list[MCQQuestion] = Field(title="Questions", description="The list of questions", example=[{"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": 0}])

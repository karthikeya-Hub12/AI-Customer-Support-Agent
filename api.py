from fastapi import FastAPI
from pydantic import BaseModel

from customer_graph import app

api = FastAPI()

class Query(BaseModel):
    question: str

@api.post("/chat")
def chat(query: Query):
    result = app.invoke({"query": query.question})
    return {"response": result["response"]}
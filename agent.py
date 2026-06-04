from support_data import COMPANY_INFO
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def get_ai_response(query):

    prompt = f"""
    You are a customer support agent.

    Use ONLY the information below.

    {COMPANY_INFO}

    Customer Question:
    {query}
    """

    response = llm.invoke(prompt)

    return response.content
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

print("API Key Loaded:", os.getenv("OPENROUTER_API_KEY")[:15])

llm = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

try:
    response = llm.invoke("Hello")
    print(response.content)

except Exception as e:
    print("\nERROR:\n")
    print(e)
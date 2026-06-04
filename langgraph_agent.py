from typing import TypedDict
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    query: str
    response: str

def faq_node(state):
    query = state["query"].lower()

    if "refund" in query:
        return {"response": "Refunds are processed within 7 business days."}

    elif "shipping" in query:
        return {"response": "Shipping takes 3-5 business days."}

    elif "return" in query:
        return {"response": "Returns accepted within 30 days."}

    return {"response": "Please contact customer support."}

graph = StateGraph(AgentState)

graph.add_node("faq", faq_node)

graph.set_entry_point("faq")

graph.add_edge("faq", END)

app = graph.compile()

while True:
    question = input("Customer: ")

    if question.lower() == "exit":
        break

    result = app.invoke({"query": question})

    print("Agent:", result["response"])
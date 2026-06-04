from typing import TypedDict
from langgraph.graph import StateGraph, END
from agent import get_ai_response

class AgentState(TypedDict):
    query: str
    response: str

def support_node(state):
    query = state["query"]

    response = get_ai_response(
        f"You are a professional customer support agent. Answer politely.\nCustomer: {query}"
    )

    return {"response": response}

graph = StateGraph(AgentState)

graph.add_node("support", support_node)

graph.set_entry_point("support")

graph.add_edge("support", END)

app = graph.compile()
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

def save_chat(user, bot):
    memory.save_context(
        {"input": user},
        {"output": bot}
    )

def get_history():
    return memory.load_memory_variables({})["history"]
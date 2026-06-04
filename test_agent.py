from agent import support_agent

while True:
    q = input("Customer: ")

    if q.lower() == "exit":
        break

    print("Agent:", support_agent(q))
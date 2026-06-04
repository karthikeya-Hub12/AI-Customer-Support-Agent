import streamlit as st
import requests

st.title("AI Customer Support Agent")

question = st.text_input("Ask a question")

if st.button("Send"):

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"question": question}
    )

    answer = response.json()

    if isinstance(answer, dict):
        st.write(answer.get("response", answer))
    else:
        st.write(answer)
import streamlit as st
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.arxiv import ArxivTools

st.title("Chat with Research Papers 🔎🤖")
st.caption("This app allows you to chat with arXiv research papers using llama3.2 running locally.")

@st.cache_resource
def get_assistant():
    return Agent(
        model=Ollama(id="llama3.2:3b"),
        tools=[ArxivTools()],
        markdown=True,
    )

assistant = get_assistant()

query = st.text_input("Enter the Search Query")

if query:
    placeholder = st.empty()
    text = ""

    for chunk in assistant.run(query, stream=True):
        if hasattr(chunk, "content") and chunk.content:
            text += chunk.content
            placeholder.markdown(text)

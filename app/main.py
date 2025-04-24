import streamlit as st
from google_tool import create_google_search_tool
from model import create_llm
from langchain.memory import ConversationBufferMemory
import asyncio
import os


os.environ['GOOGLE_API_KEY']= os.getenv('GOOGLE_API_KEY') 
os.environ['GOOGLE_CSE_ID']= os.getenv('GOOGLE_CSE_ID')
os.environ['ANTHROPIC_API_KEY'] = os.getenv('ANTHROPIC_API_KEY')


tool = create_google_search_tool()
llm = create_llm()

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

memory = st.session_state.memory

def search_and_respond_prompt(query, memory):
    results = tool.run(query)
    history = memory.load_memory_variables({}).get('history', [])
    prompt = f"""
    Histórico da conversa:
    {history}

    Com base nos resultados da pesquisa abaixo, responda diretamente à pergunta do usuário.
    Pergunta: {query}
    Resultados da pesquisa:
    {results}
    Resposta clara e direta:"""
    return prompt

st.header("🤖 Chatbot com Google Search")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Digite sua mensagem aqui")

async def stream_response(prompt):
    resposta_stream = llm.astream(prompt)
    resposta_completa = ""
    placeholder = st.empty()

    async for chunk in resposta_stream:
        resposta_completa += chunk.content
        placeholder.markdown(resposta_completa + "▌")
        await asyncio.sleep(0.02)

    placeholder.markdown(resposta_completa)
    return resposta_completa

if question:
    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append({"role": "user", "content": question})

    prompt = search_and_respond_prompt(question, memory)

    with st.chat_message("assistant"):
        resposta_final = asyncio.run(stream_response(prompt))

    memory.save_context({"input": question}, {"output": resposta_final})

    st.session_state.messages.append({"role": "assistant", "content": resposta_final})
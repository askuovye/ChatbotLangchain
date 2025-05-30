# Importar a API do Groq para ultilizar com o Langchain
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from dotenv import load_dotenv

# Carregar as variaveis do arquivo .env e proteger minhas chaves de API
load_dotenv() 

# Carregar as Chaves de API
api_key = os.getenv("OPENAI_API_KEY")
base_url = "https://api.groq.com/openai/v1"

# Inicializar o modelo de Chat "llama3" do Groq
chat_model = ChatOpenAI(
    model="llama3-8b-8192",  
    temperature=0.7,
    api_key=api_key,
    base_url=base_url
)

# Configuração do Prompt básico 
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente de IA útil."),
    ("human", "{input}")
])

# Conectar prompt + modelo
chain = prompt | chat_model

# Criar memória de chat para registrar respostas
memory = InMemoryChatMessageHistory()

# Criar executor com histórico
runnable = RunnableWithMessageHistory(
    chain,
    lambda session_id: memory,
    input_messages_key="input",
    history_messages_key="messages",
)

# Chat loop
print("Chat iniciado. Digite 'sair' para encerrar.")
while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        print("Christopher: Até mais!")
        break

    resposta = runnable.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "sessao-usuario"}}
    )

    print("Christopher:", resposta.content)
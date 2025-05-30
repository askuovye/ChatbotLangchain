# ChatbotLangchain
Python chatbot ultilizando Langchain e GroqAPI

Tecnologias e Bibliotecas Utilizadas:

LangChain	| Framework para construir aplicativos de IA usando LLMs de forma modular.
langchain_openai	| Integração com APIs compatíveis com o padrão OpenAI (como a Groq).
Groq API | Provedor de inferência de LLMs, com suporte a modelos como LLaMA 3.
Llama 3 (Meta AI) |	Modelo de linguagem open-source, altamente performático.
dotenv |	Utilitário para carregar variáveis de ambiente de um arquivo .env, garantindo segurança.
os (Python) |	Módulo padrão para acesso ao sistema operacional, como variáveis de ambiente.

Bibliotecas:

os: acessa variáveis de ambiente e manipula dados do sistema.
load_dotenv: carrega chaves de API do .env de forma segura.
ChatOpenAI: classe compatível com modelos OpenAI-like, incluindo Groq.
ChatPromptTemplate: estrutura modular de prompt formatado.
RunnableWithMessageHistory: wrapper que permite histórico de mensagens (memória).
InMemoryChatMessageHistory: armazena o histórico da conversa em memória RAM.


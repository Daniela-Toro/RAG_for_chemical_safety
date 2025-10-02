# llm_setup.py
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from config import DB_Chroma, API_KEY

# ============================
# Función para inicializar embeddings
# ============================
def init_embeddings(api_key: str = API_KEY):
    """
    Inicializa el embedding model compatible con GPT-4.
    """
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
        api_key=api_key
    )
    return embeddings


# ============================
# Función para cargar la base de datos vectorial Chroma
# ============================
def load_chroma_db(embeddings, db_path: str = DB_Chroma):
    """
    Inicializa o carga la base de datos Chroma.
    """
    # Crear carpeta si no existe
    if not os.path.exists(db_path):
        os.makedirs(db_path)

    db = Chroma(
        persist_directory=db_path,
        embedding_function=embeddings
    )
    return db


# ============================
# Función para inicializar LLM
# ============================
def init_llm(api_key: str = API_KEY):
    """
    Inicializa el modelo GPT-4o-mini para respuestas de LLM.
    """
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=api_key
    )
    return llm


# ============================
# Inicialización por defecto
# ============================
embeddings = init_embeddings()
db = load_chroma_db(embeddings)
llm = init_llm()

# config.py
import os

# ============================
# Paths de la base de datos, plantillas y outputs
# ============================
DB_Chroma = "./Chroma_DB/"
template_path = "./CO-028296-HS-2-COSHH template.xlsx"
output_Excel = "./output_Excel/"
json_excel = "./output_JSON/"
folder_documents = "./output_md_openai/"

# Asegurarse de que los directorios existen
os.makedirs(DB_Chroma, exist_ok=True)
os.makedirs(output_Excel, exist_ok=True)
os.makedirs(json_excel, exist_ok=True)
os.makedirs(folder_documents, exist_ok=True)

# ============================
# Paths de los JSON de tablas
# ============================
# Load JSON tables
JSON_PATHS = {
    "hazards": "./output_JSON/json_table_Hazards.json",
    "waste_disposal_measures": "./output_JSON/json_table_Waste_disposal_measures.json",
    "spill_management": "./output_JSON/json_table_Spill_management.json",
    "fire_procedures": "./output_JSON/json_table_Fire_procedures.json",
    "first_aid_procedures": "./output_JSON/json_table_First_aid_procedures.json",
    "storage": "./output_JSON/json_table_Storage.json"
}

# ============================
# API Key OpenAI
# ============================

API_KEY = (" ")

# ============================
# Visualización para Streamlit
# ============================

IMAGE_LOGO = "./branding/Sandoz_idk4KXMJeV_0.png"
IMAGE_BRAND = "./branding/Sandoz_idNavUNwDz_2.png"
COLORS = {
    "azul_claro": "#A8D5FF",
    "azul_medio_claro": "#5BA5FF",
    "azul_medio_oscuro": "#1C59B4",
    "azul_oscuro": "#001C4B",
    "black": "#000000",
    "white": "#FFFFFF"
}

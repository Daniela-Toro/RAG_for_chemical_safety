# app.py
import streamlit as st
import os
from config import folder_documents, COLORS, IMAGE_LOGO
from llm_setup import db
from functions import list_db_sources, filter_document, process_document

# ============================
# Page config
# ============================
st.set_page_config(page_title="SDS Analyzer", layout="wide")

# Fallbacks para colores que puedan faltar en CONFIG
WHITE = COLORS.get("white", "#FFFFFF")
AZUL_CLARO = COLORS.get("azul_claro", "#A8D5FF")
AZUL_MEDIO_CLARO = COLORS.get("azul_medio_claro", "#5BA5FF")
AZUL_MEDIO_OSCURO = COLORS.get("azul_medio_oscuro", "#1C59B4")
AZUL_OSCURO = COLORS.get("azul_oscuro", "#001C4B")

# ============================
# Styles: gradient, thin lines, centered title, larger buttons, logo sizing
# ============================
st.markdown(
    f"""
    <style>
    /* App background: black -> dark blue gradient */
    .stApp {{
        background: linear-gradient(180deg, #000000 0%, {AZUL_OSCURO} 100%);
        color: {WHITE};
        font-family: "Inter", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        min-height: 100vh;
    }}

    /* Title centered, no underline */
    .app-title {{
        text-align: center;
        color: {AZUL_CLARO};
        font-weight: 700;
        margin: 0;
        padding: 0.2rem 0 0.3rem 0;
    }}

    /* Thin elegant divider under subtitle */
    .thin-divider {{
        height: 1px;
        background: rgba(255,255,255,0.12);
        margin: 0.5rem 0 1rem 0;
        border-radius: 1px;
    }}

    /* Subtitle below title */
    .app-subtitle {{
        text-align: center;
        color: {AZUL_MEDIO_CLARO};
        margin-top: 0.15rem;
        margin-bottom: 0.25rem;
        font-weight: 500;
    }}

    /* Logo container */
    .logo-wrap {{
        display: flex;
        justify-content: center;
        margin-top: 1rem;
        margin-bottom: 0.6rem;
    }}
    .logo-wrap img {{
        max-height: 120px;
        height: auto;
    }}

    /* Preview box (centered) */
    .preview-box {{
        margin: 0 auto 1rem auto;
        max-width: 900px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
        padding: 1rem;
        border-radius: 8px;
        color: {WHITE};
        overflow: hidden;
    }}

    /* Generate section: centered title + big button */
    .generate-section {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.6rem;
        margin-top: 1rem;
        margin-bottom: 1.2rem;
    }}
    .generate-title {{
        color: {AZUL_MEDIO_CLARO};
        font-size: 1.05rem;
        font-weight: 600;
        margin: 0;
    }}

    /* Make primary buttons larger and rounded */
    .stButton>button {{
        background-color: {AZUL_MEDIO_CLARO} !important;
        color: {WHITE} !important;
        border-radius: 10px !important;
        padding: 0.7rem 1.6rem !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        border: none !important;
    }}
    .stButton>button:hover {{
        background-color: {AZUL_MEDIO_OSCURO} !important;
        transition: 0.15s;
    }}

    /* Inputs style */
    .stTextInput>div>div>input,
    .stSelectbox>div>div>div {{
        background-color: rgba(255,255,255,0.04);
        color: {WHITE};
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 8px;
        padding: 0.5rem;
    }}

    /* Small helper text style */
    .helper-small {{
        color: rgba(255,255,255,0.7);
        text-align:center;
        font-size: 0.9rem;
        margin-top: 0.25rem;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================
# Header: logo + title + subtitle + thin divider
# ============================
# Logo: use st.image so Streamlit maneje la imagen correctamente
col_logo = st.container()
with col_logo:
    try:
        st.image(IMAGE_LOGO, width=180)  # ajusta width si quieres más grande
    except Exception:
        # si la ruta falla, muestra un texto alternativo
        st.markdown("<div style='text-align:center;color:rgba(255,255,255,0.5)'>[Logo not available]</div>", unsafe_allow_html=True)

# Centered title and subtitle
st.markdown(f"<h1 class='app-title'>SDS Analyzer</h1>", unsafe_allow_html=True)
st.markdown(f"<div class='app-subtitle'>Analyze SDS documents and generate COSHH evaluation Excel</div>", unsafe_allow_html=True)

# Thin divider under subtitle (white, very thin)
st.markdown("<div class='thin-divider'></div>", unsafe_allow_html=True)

# ============================
# Step 1: Selection (Search or DB)
# ============================
st.markdown("### 1. Select the method to identify the chemical", unsafe_allow_html=True)
option = st.radio("Choose a method:", ("Search by name", "Select from database"), index=0)

# session state initialization
if "source_match" not in st.session_state:
    st.session_state.source_match = None
if "content" not in st.session_state:
    st.session_state.content = None
if "excel_path" not in st.session_state:
    st.session_state.excel_path = None

# Search by name with placeholder example
if option == "Search by name":
    query = st.text_input("Enter the chemical product name:", placeholder="Example: Acetone, Ethanol, 2-Butoxyethanol...")
    search_btn = st.button("Search")
    if search_btn:
        if not query:
            st.warning("Please enter a product name.")
        else:
            try:
                matched, content = filter_document(query, db)
                st.session_state.source_match = matched
                st.session_state.content = content
                st.success(f"Matching document found: {matched}")
            except Exception as e:
                st.error(f"No document found: {e}")

# Select from DB with instructive default option
elif option == "Select from database":
    # list_db_sources may return set or list, ensure list
    sources = list(list_db_sources(db))
    select_options = ["-- Select product from database --"] + sources
    selected = st.selectbox("Select product:", select_options, index=0)
    if selected and selected != select_options[0]:
        try:
            doc_path = os.path.join(folder_documents, selected)
            with open(doc_path, "r", encoding="utf-8") as f:
                content = f.read()
            st.session_state.source_match = selected
            st.session_state.content = content
            st.success(f"Selected document: {selected}")
        except Exception as e:
            st.error(f"Error loading file: {e}")

# ============================
# Preview (centered, truncated) - appears automatically after selecting/searching
# ============================
if st.session_state.source_match and st.session_state.content:
    # truncate content: first N lines
    max_lines = 40
    lines = st.session_state.content.splitlines()
    truncated = "\n".join(lines[:max_lines])
    if len(lines) > max_lines:
        truncated += "\n\n... (truncated preview) ..."

    # Render preview box (render markdown so .md is shown)
    st.markdown(
        f"""
        <div class="preview-box">
            <strong>Document preview:</strong>
            <div style="margin-top:0.5rem;">
                <!-- Render the truncated markdown content -->
                {st.session_state.content[:2000] if len(st.session_state.content) < 2000 else st.session_state.content[:2000] + '\n\n...'}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Small helper line under preview
    st.markdown('<div class="helper-small">Preview shows first ~40 lines of the document</div>', unsafe_allow_html=True)

    # ============================
    # Generate section (Step 2: Process and Generate Excel)
    # ============================
    st.markdown("### 2. Process and Generate Excel", unsafe_allow_html=True)

    # Center the button using container
    generate_col = st.container()
    with generate_col:
        generate = st.button("Generate Excel")  # styled large by CSS above

    # If user clicks generate
    if generate:
        st.session_state.excel_path = None
        with st.spinner("Processing document and generating Excel..."):
            try:
                updated_jsons, excel_path = process_document(
                    st.session_state.source_match, st.session_state.content
                )
                if excel_path:
                    st.session_state.excel_path = excel_path
                    st.success("✅ Excel successfully generated.")
                else:
                    st.warning("⚠️ Excel could not be generated.")
            except Exception as e:
                st.error(f"❌ Error during processing: {e}")

# ============================
# Download button shown once the excel is available
# ============================
if st.session_state.excel_path:
    try:
        with open(st.session_state.excel_path, "rb") as f:
            excel_bytes = f.read()
        st.download_button(
            label="📥 Download Excel",
            data=excel_bytes,
            file_name=os.path.basename(st.session_state.excel_path),
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    except Exception as e:
        st.error(f"Error reading generated Excel: {e}")


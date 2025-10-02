# ⚗️ SDS Analyzer – Automated Chemical Risk Assessment (COSHH)  

This repository contains the code and resources for my **Master’s Thesis (TFM)** in *Data Science, Big Data & Business Analytics*.  
The project consists of developing an application based on **Retrieval-Augmented Generation (RAG)** that allows:  

- 📄 Analyzing **Safety Data Sheets (SDS/MSDS)**.  
- 🔎 Extracting, normalizing, and structuring critical information.  
- 📊 Automatically generating **COSHH** assessments ready for corporate use.  

The solution was developed in collaboration with the pharmaceutical company **Sandoz**.  

---

## 📂 Project Structure  

The repository includes the main code files and notebooks:

- `app.py` → main **Streamlit** application, entry point for the user interface.  
- `config.py` → configuration parameters (colors, paths, logos, etc.).  
- `functions.py` → helper functions for business logic (processing, normalization, etc.).  
- `llm_setup.py` → **LangChain** setup and connection to the OpenAI API.  
- `utils.py` → general utilities.  
- `requirements.txt` → libraries required to set up the environment.  
- `run_app.bat` → script to easily run the application on Windows.  
- `Notebooks/` → contains notebooks used in the prototyping and testing phase:
  - `Create_JSONs.ipynb`  
  - `Create_RAG.ipynb`  
  - `Fill_Excel.ipynb`  

⚠️ **Important Note**:  
For **security and confidentiality** reasons, the following are not included in the repository:
- The vector database (**ChromaDB**) used in the project.  
- Corporate template files (e.g., `CO-028296-HS-2-COSHH template.xlsx`).  
- Original chemical safety documents (SDS/MSDS).  

These resources are only available in the corporate environment to ensure privacy and regulatory compliance.  

---

### 🔧 Tech Stack  
- **Python 3.10+**  
- [Streamlit](https://streamlit.io/) → Interactive web interface.  
- [LangChain](https://www.langchain.com/) → Orchestration of prompts, embeddings, and pipelines.  
- [ChromaDB](https://docs.trychroma.com/) → Vector database for semantic search.  
- [OpenAI API](https://platform.openai.com/) → State-of-the-art language models.  
- [RecursiveCharacterTextSplitter](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/) → Document chunking and preprocessing.  
- **Pandas, OpenPyXL, PDFPlumber** → Data handling, Excel, and PDF processing.  

---

## 🚀 Quick Start on Windows

The repository includes a `run_app.bat` script that automates the process:

- Activates the virtual environment.
- Launches the application in Streamlit.

You only need to double-click `run_app.bat` (after creating and activating the environment beforehand).

### Install Dependencies
```bash
pip install -r requirements.txt


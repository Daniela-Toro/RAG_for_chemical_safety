@echo off

REM Ir al directorio del proyecto
cd /d %~dp0

REM Ejecutar Streamlit
start "" streamlit run app.py

# main.py
from pywinauto.application import Application
from Telas.Login import executar_login
from dotenv import load_dotenv
import os

APP_PATH = r"C:\Salux\SxSigma - Portal\portal.exe"
WORK_DIR = r"C:\Salux\SxSigma - Portal"

load_dotenv()
usuario = os.getenv("USUARIO_SIGMA")
senha   = os.getenv("SENHA_SIGMA")

# Use backend="win32" aqui
#Setar o work_dir para evitar problemas de DLL
app = Application(backend="win32").start(cmd_line=APP_PATH, work_dir=WORK_DIR)

# Popup de erro, se houver
dlg = app.window(title='Erro')
if dlg.exists(timeout=8):
    dlg.child_window(title="OK", class_name="Button").click_input()
try:
    executar_login(app, usuario, senha)
except Exception as e:
    print(f"Erro durante o login: {e}")
    app.kill()
    exit(1)


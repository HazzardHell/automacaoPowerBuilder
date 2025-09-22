from Telas.sigmaActions import SigmaActions
from Telas.Login import executar_login
from Telas.mainMenu import MainMenu
from dotenv import load_dotenv
import os

APP_PATH = r"C:\Salux\SxSigma - Portal\portal.exe"
WORK_DIR = r"C:\Salux\SxSigma - Portal"

load_dotenv()
usuario = os.getenv("USUARIO_SIGMA")
senha   = os.getenv("SENHA_SIGMA")

sigma = SigmaActions(APP_PATH, WORK_DIR)

dlg = sigma.try_get_window(title_re="Erro", timeout=8)
if dlg:
    dlg.child_window(title="OK", class_name="Button").click_input()
    print("Popup de erro fechado.")
else:
    print("Nenhum popup de erro apareceu.")


# Login usando a API do Sigma
try:
    executar_login(sigma, usuario, senha)
except Exception as e:
    print(f"Erro durante o login: {e}")
    sigma.kill()
    exit(1)

try:
    # Agora é possível continuar chamando outros métodos
    sigma.wait_for_window("INFOSAUDE.*")
    print("Tela principal pronta.")
    MenuSigma = MainMenu(sigma)
    MenuSigma.mapear_menus_principais()
except Exception as e:
    print(f"Erro durante o mapeamento dos menus: {e}")
    sigma.kill()
    exit(1)


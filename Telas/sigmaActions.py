# Telas/sigma_actions.py
from pywinauto.application import Application
from pywinauto import Desktop

class SigmaActions:
    def __init__(self, app_path: str, work_dir: str = None):
        """
        Inicia a aplicação Sigma e guarda a instância do pywinauto.Application.
        """
        self.app = Application(backend="win32").start(cmd_line=app_path, work_dir=work_dir)
        print("Aplicação Sigma iniciada.")

    # def get_window(self, title_re: str):
    #     """Retorna uma janela específica pelo título (regex)."""
    #     return self.app.window(title_re=title_re)

    def listar_todos_elementos(self):
        """Imprime todos os controles da tela principal para inspeção."""
        main_win = self.app.window(title_re="INFOSAUDE.*")
        main_win.wait("ready", timeout=60)

        print("\n=== TODOS OS ELEMENTOS DA TELA PRINCIPAL ===")
        main_win.print_control_identifiers()

    def kill(self):
        """Encerra a aplicação Sigma."""
        self.app.kill()
        print("Aplicação Sigma encerrada.")

    def get_window(self, title_re: str):
        win = self.app.window(title_re=title_re)
        win.wait("enabled", timeout=60)
        return win

    def list_controls(self, title_re: str):
        win = self.get_window(title_re)
        win.print_control_identifiers()

    def set_text(self, element, text: str):
        """Foca e insere texto em um controle Edit."""
        element.set_focus()
        element.set_text(text)

    def type_keys(self, window, keys: str, pause=0.1):
        """Envia teclas para uma janela."""
        window.set_focus()
        window.type_keys(keys, pause=pause)

    def read_text(self, element) -> str:
        """Retorna o texto de um controle (ex.: Edit)."""
        return element.window_text()
    
    def wait_for_window(self, title_re: str, timeout: int = 60):
        """Espera uma janela específica aparecer e retorna o objeto."""
        win = self.app.window(title_re=title_re)
        win.wait("ready", timeout=timeout)
        return win

    def top_window(self):
        """Retorna a janela que está no topo (ativa)."""
        return self.app.top_window()
    
    def click_button(self, window, title: str = None, class_name: str = "Button"):
        """
        Clica em um botão pelo título ou class_name.
        Se 'title' for None, clica no primeiro botão encontrado.
        """
        if title:
            btn = window.child_window(title=title, class_name=class_name)
        else:
            btn = window.child_window(class_name=class_name)
        btn.wait("enabled", timeout=30)
        btn.click_input()
        return btn
    
    from pywinauto import Desktop

    def capture_screenshot(self, file_path: str):
        """Salva um print da tela inteira."""
        Desktop(backend="win32").capture_as_image().save(file_path)
        print(f"Screenshot salvo em: {file_path}")

    def select_menu(self, window, path: str):
        """
        Seleciona um item de menu clássico Win32.
        Exemplo de path: "Cadastro->Paciente Simplificado".
        """
        window.menu_select(path)
        print(f"Menu '{path}' selecionado.")

    def wait_until_exists(self, window, control_title: str, control_class: str, timeout: int = 30):
        """
        Espera até que um controle específico exista.
        """
        return window.child_window(title=control_title, class_name=control_class).wait("exists enabled visible", timeout=timeout)
    
    def close_window(self, window):
        """Fecha a janela informada."""
        window.close()
        print("Janela fechada.")

    def try_get_window(self, title_re: str, timeout: int = 5):
        """
        Tenta obter uma janela pelo título (regex).
        Retorna a janela se existir, ou None se não encontrar no tempo limite.
        """
        win = self.app.window(title_re=title_re)
        if win.exists(timeout=timeout):
            return win
        return None





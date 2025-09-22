from Telas.utils.export_json import export_controls_to_json
from .utils.filesystem import criar_pasta
from .sigmaActions import SigmaActions  # mantém a consistência de imports
from .utils.gui_actions import GUIActions  # mantém a consistência de imports
from DTO.gestaoClientes import MODULES
import os

class MainMenu:
    def __init__(self, sigma: SigmaActions):
        # Guarda a instância de SigmaActions e a aplicação em execução
        self.sigma = sigma
        self.app = sigma.app   # objeto pywinauto.Application
        self.gui = GUIActions() # objeto para ações de GUI (PyAutoGUI)

    def testeModulo(self):
        """
        Testa abrir o módulo "Ambulatorio" como exemplo.
        """
        try:
            self.open_module("ambulatorio")
        except Exception as e:
            print(f"Erro ao abrir módulo: {e}")
            raise e

    def open_module(self, module_name: str, timeout: int = 10):
        """
        Abre um módulo pelo nome, usando os caminhos definidos em DTO.gestaoClientes.
        """
        # normaliza a chave para minúsculas
        key = module_name.lower()
        if key not in MODULES:
            raise ValueError(f"Módulo desconhecido: {module_name}")

        data = MODULES[key]

        # monta caminhos completos para as imagens
        base_path = os.path.join("Telas", "areas")
        menu_img = os.path.join(base_path, data["menu_section"])
        module_img = os.path.join(base_path, "modulos", data["module_image"])

        print(f"Abrindo módulo: {module_name}")
        print(f"  menu lateral: {menu_img}")
        print(f"  módulo: {module_img}")

        if not os.path.exists(menu_img):
            raise FileNotFoundError(f"Imagem do menu não encontrada: {menu_img}")
        # clica primeiro no menu lateral
        # if not self.gui.click_image(menu_img, timeout=timeout):
        #     raise RuntimeError(f"Não foi possível localizar a seção do menu: {menu_img}")

        if not os.path.exists(module_img):
            raise FileNotFoundError(f"Imagem do módulo não encontrada: {module_img}")
        # depois clica no botão do módulo
        if not self.gui.click_image(module_img, timeout=timeout):
            raise RuntimeError(f"Não foi possível localizar o módulo: {module_img}")

        print(f"✅ Módulo '{module_name}' aberto com sucesso.")


    def clicar_botao_por_imagem(self, nome_imagem: str, timeout: int = 10) -> bool:
        """
        Localiza e clica em um botão com base na imagem salva.

        :param nome_imagem: Nome do arquivo da imagem (ex.: "Ambulatorio.png").
        :param timeout: Tempo máximo (segundos) para localizar o botão.
        :return: True se o clique for bem-sucedido, False se não encontrar.
        """
        print(f"Procurando e clicando no botão: {nome_imagem}")
        if self.gui.click_image(nome_imagem, timeout=timeout):
            print(f"✅ Clique realizado: {nome_imagem}")
            return True
        else:
            print(f"❌ Não foi possível localizar: {nome_imagem}")
            return False


    # def mapear_menus_principais(self, base_path: str = "Menus"):
    #     # """
    #     # Percorre os menus principais da tela inicial (INFOSAUDE...) e cria
    #     # pastas correspondentes, incluindo submódulos.

    #     # """
    #     # try:

    #     #     """
    #     #     Ponto inicial: chama testes para identificar onde estão
    #     #     os botões reais (PowerBuilder pbdw ou WebView).
    #     #     """

    #     #     main_win = self.app.window(title_re="INFOSAUDE.*")
    #     #     main_win.wait("ready", timeout=60)
    #     #     print("\n=== Investigando a tela principal ===")

    #     #     # Teste hipótese 1: container pbdw
    #     #     self.testar_container_pbdw(main_win)

    #     #     # Teste hipótese 2: componente WebView/HTML
    #     #     self.testar_webview_uia()

    #     #     return
             
    #     # except Exception as e:
    #     #     print(f"Erro ao criar/verificar pasta base '{base_path}': {e}")
    #     #     raise

    #     try:
    #         main_win = self.app.window(title_re="INFOSAUDE.*")
    #         main_win.wait("ready", timeout=60)

    #         print("\nMenus principais encontrados:")
    #         # main_win.print_control_identifiers()

    #         # Exporta o mapa completo de controles para JSON
    #         export_controls_to_json(main_win, "menus/mapa_completo.json")

    #         botoes_menu = [
    #             c for c in main_win.descendants() if c.friendly_class_name() == "Button"
    #         ]
    #         print("Menus principais:", [b.window_text() for b in botoes_menu])


    #         for botao in botoes_menu:
    #             nome_menu = botao.window_text().strip()
    #             if not nome_menu:
    #                 continue

    #             pasta_menu = criar_pasta(base_path, nome_menu)
    #             print(f"Pasta criada/verificada: {pasta_menu}")

    #             # Abre o menu e mapeia submódulos
    #             botao.click_input()
    #             sub_win = self.app.top_window()
    #             sub_botoes = sub_win.children(control_type="Button")

    #             for sub in sub_botoes:
    #                 nome_sub = sub.window_text().strip()
    #                 if nome_sub:
    #                     sub_path = criar_pasta(pasta_menu, nome_sub)
    #                     print(f"  Subpasta criada/verificada: {sub_path}")

    #     except Exception as e:
    #         print(f"Erro ao mapear menus principais: {e}")
    #         raise

    # def investigar_container(self):
    #     main_win = self.app.window(title_re="INFOSAUDE.*")
    #     main_win.wait("ready", timeout=60)

    #     # Liste tudo de primeiro nível, para achar nomes suspeitos
    #     print("\n--- Controles diretos da janela ---")
    #     for c in main_win.children():
    #         print(c.friendly_class_name(), "-", c.class_name(), "-", c.window_text())

    #     # Procure especificamente por pbdw (PowerBuilder DataWindow)
    #     pbdw_controls = [c for c in main_win.descendants()
    #                     if "pbdw" in c.class_name().lower()]
    #     print("\n--- Possíveis containers pbdw ---")
    #     for c in pbdw_controls:
    #         print(c.class_name(), c.window_text(), c.element_info.rectangle)

    #         # Salva screenshot do container para ver se é a área dos botões
    #         img = c.capture_as_image()
    #         img.save(f"pbdw_{c.handle}.png")

    #         # Tenta detalhar a árvore interna do controle
    #         try:
    #             c.print_control_identifiers()
    #         except Exception as e:
    #             print("Não conseguiu detalhar:", e)


    # # ---------------------- HIPÓTESE 1 ----------------------
    # def testar_container_pbdw(self, main_win):
    #     """
    #     Procura containers do tipo PowerBuilder DataWindow (pbdw)
    #     e tenta extrair seus filhos, salvar prints e JSON.
    #     """
    #     print("\n--- Testando hipótese 1: container pbdw ---")
    #     try:
    #         pbdw_controls = [c for c in main_win.descendants()
    #                          if "pbdw" in c.class_name().lower()]
    #         print(f"Containers pbdw encontrados: {len(pbdw_controls)}")

    #         for c in pbdw_controls:
    #             print(f"  pbdw: {c.class_name()} handle={c.handle}")
    #             # Captura imagem do container
    #             try:
    #                 img = c.capture_as_image()
    #                 img.save(f"pbdw_{c.handle}.png")
    #                 print(f"    -> screenshot salvo pbdw_{c.handle}.png")
    #             except Exception as e:
    #                 print(f"    -> Falhou screenshot: {e}")

    #             # Exporta controles filhos para JSON
    #             try:
    #                 export_controls_to_json(c, f"menus/pbdw_{c.handle}.json")
    #             except Exception as e:
    #                 print(f"    -> Falhou export JSON: {e}")

    #             # Dump rápido no console
    #             try:
    #                 c.print_control_identifiers()
    #             except Exception as e:
    #                 print(f"    -> Falhou print identifiers: {e}")

    #     except Exception as e:
    #         print(f"Erro na investigação de pbdw: {e}")

    # # ---------------------- HIPÓTESE 2 ----------------------
    # def testar_webview_uia(self):
    #     """
    #     Tenta anexar a mesma janela usando backend 'uia' para ver
    #     se há um controle WebView/HTML oculto.
    #     """
    #     print("\n--- Testando hipótese 2: backend UIA/WebView ---")
    #     try:
    #         from pywinauto import Application
    #         # Conecta na mesma janela mas com backend 'uia'
    #         app_uia = Application(backend="uia").connect(title_re="INFOSAUDE.*")
    #         win_uia = app_uia.window(title_re="INFOSAUDE.*")
    #         win_uia.wait("ready", timeout=60)
    #         print("Conexão UIA feita com sucesso.")
    #         # Lista classes que lembram WebView/ActiveX
    #         suspeitos = []
    #         for c in win_uia.descendants():
    #             cls = c.element_info.class_name or ""
    #             if any(k in cls.lower() for k in [
    #                 "internet explorer", "edge", "webview", "chrome", "cef", "mshtml"
    #             ]):
    #                 suspeitos.append((cls, c.window_text()))
    #         print(f"Controles suspeitos de WebView: {suspeitos}")
    #         # Salva todo o mapeamento em JSON para inspecionar
    #         export_controls_to_json(win_uia, "menus/controles_uia.json")
    #     except Exception as e:
    #         print(f"Erro na investigação com backend UIA: {e}")


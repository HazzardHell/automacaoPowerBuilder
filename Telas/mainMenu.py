from Telas.utils.export_json import export_controls_to_json
from .utils.filesystem import criar_pasta
from .sigmaActions import SigmaActions  # mantém a consistência de imports

class MainMenu:
    def __init__(self, sigma: SigmaActions):
        # Guarda a instância de SigmaActions e a aplicação em execução
        self.sigma = sigma
        self.app = sigma.app   # objeto pywinauto.Application

    def mapear_menus_principais(self, base_path: str = "Menus"):
        """
        Percorre os menus principais da tela inicial (INFOSAUDE...) e cria
        pastas correspondentes, incluindo submódulos.
        """
        try:
            main_win = self.app.window(title_re="INFOSAUDE.*")
            main_win.wait("ready", timeout=60)

            print("\nMenus principais encontrados:")
            # main_win.print_control_identifiers()

            # Exporta o mapa completo de controles para JSON
            export_controls_to_json(main_win, "menus/mapa_completo.json")

            botoes_menu = [
                c for c in main_win.descendants() if c.friendly_class_name() == "Button"
            ]
            print("Menus principais:", [b.window_text() for b in botoes_menu])


            for botao in botoes_menu:
                nome_menu = botao.window_text().strip()
                if not nome_menu:
                    continue

                pasta_menu = criar_pasta(base_path, nome_menu)
                print(f"Pasta criada/verificada: {pasta_menu}")

                # Abre o menu e mapeia submódulos
                botao.click_input()
                sub_win = self.app.top_window()
                sub_botoes = sub_win.children(control_type="Button")

                for sub in sub_botoes:
                    nome_sub = sub.window_text().strip()
                    if nome_sub:
                        sub_path = criar_pasta(pasta_menu, nome_sub)
                        print(f"  Subpasta criada/verificada: {sub_path}")

        except Exception as e:
            print(f"Erro ao mapear menus principais: {e}")
            raise

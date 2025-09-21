from pywinauto.application import Application

def executar_login(app: Application, usuario: str, senha: str):
    try:
        print("Iniciando processo de login...")

        login_win = app.window(title_re="Conectar.*")
        login_win.wait("enabled", timeout=30)
        login_win.set_focus()

        edits = login_win.children(class_name="Edit")
        print(f"Foram encontrados {len(edits)} campos Edit")

        # Usuário
        # edits[0].wait("visible enabled", timeout=10)
        edits[0].set_focus()
        edits[0].set_text(usuario)
        print(f"Usuário '{usuario}' inserido.")

        # Senha
        # edits[1].wait("visible enabled", timeout=10)
        edits[1].set_focus()
        edits[1].set_text(senha)
        print("Senha inserida.")

        # Unidade (se houver)
        if len(edits) > 2:
            # edits[2].wait("visible enabled", timeout=10)
            login_win.set_focus()
            # Seleciona a unidade
            login_win.type_keys("{TAB}{DOWN}{DOWN}", pause=0.1)

            # Confere o valor antes de dar ENTER
            selected_unit = edits[2].window_text()
            print("Valor atual do campo unidade:", selected_unit)
            while True:
                if "SALUX HOSPITAL UM" in selected_unit:
                    print("Unidade confirmada corretamente.")
                    login_win.type_keys("{ENTER}")
                    break
                else:
                    print("A unidade ainda não está correta:", selected_unit)
                                        
                    login_win.set_focus()
                    # Seleciona a unidade
                    login_win.type_keys("{TAB}{DOWN}{DOWN}", pause=0.1)

                    # Confere o valor antes de dar ENTER
                    selected_unit = edits[2].window_text()
        
        print("Login realizado com sucesso.")       
        
    except Exception as e:
        print(f"Erro durante o login: {e}")
        raise

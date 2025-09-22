from Telas.sigmaActions import SigmaActions

def executar_login(sigma: SigmaActions, usuario: str, senha: str):
    try:
        print("Iniciando processo de login...")

        login_win = sigma.get_window("Conectar.*")

        edits = login_win.children(class_name="Edit")
        print(f"Foram encontrados {len(edits)} campos Edit")

        # Usuário
        sigma.set_text(edits[0], usuario)
        print(f"Usuário '{usuario}' inserido.")

        # Senha
        sigma.set_text(edits[1], senha)
        print("Senha inserida.")

        # Unidade
        if len(edits) > 2:
            while True:
                sigma.type_keys(login_win, "{TAB}{DOWN}{DOWN}")
                selected_unit = sigma.read_text(edits[2])
                print("Valor atual do campo unidade:", selected_unit)

                if "SALUX HOSPITAL UM" in selected_unit:
                    print("Unidade confirmada corretamente.")
                    sigma.type_keys(login_win, "{ENTER}")
                    break
                else:
                    print("A unidade ainda não está correta, tentando novamente...")

        print("Login realizado com sucesso.")
    except Exception as e:
        print(f"Erro durante o login: {e}")
        raise

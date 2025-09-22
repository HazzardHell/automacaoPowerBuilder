import os
from Telas.sigmaActions import SigmaActions

class ScriptGenerator(SigmaActions):
    def __init__(self):
        super().__init__()

    def create_script(self, file_path: str, content: str, overwrite: bool = False) -> str:
        """
        Cria um arquivo .py no caminho indicado com o conteúdo informado.

        :param file_path: Caminho completo do arquivo a ser criado (ex: 'C:/Projetos/teste.py').
        :param content: Código Python que será escrito no arquivo.
        :param overwrite: Se False, não sobrescreve caso o arquivo já exista.
        :return: Caminho absoluto do arquivo criado.
        """
        # Garante extensão .py
        if not file_path.endswith(".py"):
            file_path += ".py"

        # Cria pastas se não existirem
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Se não for para sobrescrever e o arquivo já existir, aborta
        if not overwrite and os.path.exists(file_path):
            raise FileExistsError(f"O arquivo '{file_path}' já existe. "
                                  f"Passe overwrite=True para sobrescrever.")

        # Escreve o conteúdo no arquivo
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return os.path.abspath(file_path)

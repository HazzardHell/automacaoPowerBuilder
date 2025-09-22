import pyautogui
import time
import os

class GUIActions:
    """
    Abstrai operações comuns de automação de tela usando PyAutoGUI.
    """

    def __init__(self, default_image_path: str = "imagens_botoes"):
        # pasta onde ficam as imagens dos botões
        self.default_image_path = default_image_path

    # ----------------- Captura -----------------
    def screenshot(self, name: str = "screenshot.png", region=None):    
        """
        Captura a tela inteira ou uma região específica e salva em default_image_path.
        """
        path = os.path.join(self.default_image_path, name)
        shot = pyautogui.screenshot(region=region)
        shot.save(path)
        print(f"Screenshot salvo em {path}")
        return path

    # ----------------- Movimentação e clique -----------------
    def click_center(self, region):
        """Clica no centro de uma região (left, top, width, height)."""
        x, y = pyautogui.center(region)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Clique realizado em ({x}, {y})")

    def click_image(self, image_name: str, timeout: int = 10, confidence: float = 0.20):
        """
        Localiza e clica na imagem informada.
        Retorna True se encontrou, False se não encontrou no tempo limite.
        """
        img_path = os.path.join(self.default_image_path, image_name)
        if not os.path.exists(img_path):
            print(f"Imagem não encontrada: {img_path}")
            return False

        print(f"Procurando: {img_path}")
        start = time.time()
        while time.time() - start < timeout:
            region = pyautogui.locateOnScreen(img_path, confidence=confidence)
            if region:
                self.click_center(region)
                print(f"Imagem {image_name} clicada com sucesso.")
                return True
            time.sleep(0.5)

        print(f"Imagem {image_name} não encontrada em {timeout}s.")
        return False

    # ----------------- Digitação -----------------
    def type_text(self, text: str, interval: float = 0.05):
        """Digita texto com atraso entre as teclas."""
        pyautogui.typewrite(text, interval=interval)
        print(f"Texto digitado: {text}")

    def press_key(self, key: str):
        """Pressiona uma tecla específica."""
        pyautogui.press(key)
        print(f"Tecla pressionada: {key}")

    def hotkey(self, *keys):
        """Pressiona uma combinação de teclas (ex.: ctrl, s)."""
        pyautogui.hotkey(*keys)
        print(f"Combinação de teclas pressionada: {keys}")

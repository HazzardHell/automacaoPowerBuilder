import json
import os
from pywinauto.base_wrapper import BaseWrapper

def export_controls_to_json(wrapper: BaseWrapper, output_path: str):
    """
    Constrói um dicionário recursivo de todos os controles de uma janela
    e salva como JSON em output_path.
    """
    def build_tree(elem: BaseWrapper):
        # Evita travar se não tiver texto
        title = elem.window_text() or "none"
        node = {
            "title": title,
            "class_name": elem.friendly_class_name(),
            "children": []
        }

        # Recorre nos filhos
        try:
            for child in elem.children():
                node["children"].append(build_tree(child))
        except Exception:
            # alguns controles podem não permitir children()
            pass

        return node

    data = build_tree(wrapper)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Mapa de controles exportado para: {output_path}")

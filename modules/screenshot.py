from pathlib import Path
from PIL import Image
import io, datetime

def take_screenshot(driver, folder="prints", name="print"):
    folder_path = Path(folder)
    folder_path.mkdir(exist_ok=True)
    png = driver.get_screenshot_as_png()
    image = Image.open(io.BytesIO(png))
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    image.save(folder_path / f"{name}_{ts}.png")

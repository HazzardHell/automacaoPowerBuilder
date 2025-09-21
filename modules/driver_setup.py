from appium import webdriver
from appium.options.common import AppiumOptions   # <-- esta é a classe correta

def start_driver(app_path):
    options = AppiumOptions()
    options.set_capability("platformName", "Windows")
    options.set_capability("deviceName", "WindowsPC")
    options.set_capability("app", app_path)

    return webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

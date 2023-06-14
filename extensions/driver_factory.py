import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .driver_listener import DriverListener
from extensions.driver_extended import DriverExtended
from base import utils


class DriverFactory:

    @staticmethod
    def get_driver(config) -> DriverExtended:
        if config["browser"] == "local":
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('window-size=1920x1080')
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("prefs", {
                "download.default_directory": os.getcwd(),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            })
            if config["headless_mode"] is True:
                options.add_argument("--headless")
                options.add_argument('--disable-gpu')
                options.add_argument('window-size=1920x1080')
            driver = DriverExtended(
                webdriver.Chrome(ChromeDriverManager().install(), options=options),
                DriverListener(), config
            )
            driver.maximize_window()
            return driver

        raise Exception("Provide valid driver name")

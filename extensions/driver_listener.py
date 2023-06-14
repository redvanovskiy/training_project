from datetime import datetime
from selenium.webdriver.support.events import AbstractEventListener
import logging
import os
import shutil


class DriverListener(AbstractEventListener):

    shutil.rmtree('reports', ignore_errors=True)
    log_filename = datetime.now().strftime("%Y.%m.%d %H:%M")
    report_dir = "reports"
    try:
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
    except (Exception, RuntimeError):
        logging.error('Exception Occurred when creating reports directory')
    logging.basicConfig(
        filename=f"reports/logs_driver_{log_filename}.log",
        format="%(asctime)s: %(levelname)s: %(message)s",
        level=logging.INFO
    )

    def __init__(self):
        self.logger = logging.getLogger("selenium")

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Navigating to {url}")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"{url} opened")

    def before_find(self, by, value, driver):
        self.logger.info(f"Searching for element by {by} {value}")

    def after_find(self, by, value, driver):
        self.logger.info(f"Element by {by} {value} found")

    def before_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.logger.info(f"Clicking on {element.get_attribute('class')}")
        else:
            self.logger.info(f"Clicking on {element.get_attribute('text')}")

    def after_click(self, element, driver):
        self.logger.info("Clicked")

    def before_change_value_of(self, element, driver):
        self.logger.info(f"{element.get_attribute('text')} value changed")

    def before_close(self, driver):
        self.logger.info("Driver closing tab")

    def after_close(self, driver):
        self.logger.info("Driver closed tab")

    def before_quit(self, driver):
        self.logger.info("Driver stopping")

    def after_quit(self, driver):
        self.logger.info("Driver stopped")

    def on_exception(self, exception, driver):
        self.logger.info(exception)

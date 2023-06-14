from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from .utils import *
import datetime
import logging
import time


class Base:
    
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger("selenium")

    def screenshot(self):
        test_name = os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0].replace("test_", "")
        file_name = test_name + "_" + str((datetime.date.today().strftime("%Y-%m-%d"))) + ".png"
        scr_dir = "../reports/screenshots/"
        relative_file_name = scr_dir + file_name
        current_dir = os.path.dirname(__file__)
        destination_file = os.path.join(current_dir, relative_file_name)
        destination_dir = os.path.join(current_dir, scr_dir)
        try:
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            self.driver.save_screenshot(destination_file)
            self.logger.info(f"Screenshot `{file_name}` saved to `{scr_dir}`")
        except (Exception, RuntimeError, ScreenshotException):
            raise

    def open(self):
        try:
            self.driver.load()
        except (NoSuchWindowException, TimeoutException):
            self.screenshot()
            raise

    def page_loaded(self):
        start_time = time.time()
        while time.time() - start_time < 15:
            page_state = self.driver.execute_script('return document.readyState;')
            if page_state == 'complete':
                break
            else:
                time.sleep(1)

    def get(self, url):
        try:
            self.driver.get(url)
        except (NoSuchWindowException, TimeoutException):
            self.screenshot()
            raise

    def refresh(self):
        try:
            self.driver.refresh()
        except (NoSuchWindowException, TimeoutException):
            self.screenshot()
            raise

    def back(self):
        try:
            self.driver.back()
        except (NoSuchWindowException, TimeoutException):
            self.screenshot()
            raise

    def forward(self):
        try:
            self.driver.forward()
        except (NoSuchWindowException, TimeoutException):
            self.screenshot()
            raise

    def title(self):
        try:
            return self.driver.title
        except (NoSuchWindowException, TimeoutException):
            self.screenshot()
            raise

    def url(self):
        try:
            return self.driver.current_url
        except (NoSuchWindowException, TimeoutException):
            self.screenshot()
            raise

    def find_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            self.screenshot()
            raise

    def visible(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return bool(element)
        except (NoSuchElementException, TimeoutException):
            self.screenshot()
            raise

    def not_visible(self, locator, timeout=2):
        try:
            return WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            self.screenshot()
            raise

    def enabled(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            self.screenshot()
            raise

    def disabled(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until_not(EC.element_to_be_clickable(locator))
        except (NoSuchElementException, TimeoutException):
            self.screenshot()
            raise

    def clickable(self, locator, timeout=15):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException, StaleElementReferenceException):
            self.screenshot()
            raise

    def click(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            self.screenshot()
            raise

    def appeared(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            self.screenshot()
            raise

    def disappeared(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            self.screenshot()
            raise

    def get_attribute(self, locator, attribute_name):
        try:
            return self.driver.find_element(locator).get_attribute(attribute_name)
        except (NoSuchElementException, NoSuchAttributeException, TimeoutException):
            self.screenshot()
            raise

    def hover_to(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return ActionChains(self.driver).move_to_element(element).perform()
        except (NoSuchElementException, TimeoutException):
            self.screenshot()
            raise

    def clear_field(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).clear()
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            self.screenshot()
            raise

    def enter_text(self, locator, text, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)) \
                .send_keys(text)
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            self.screenshot()
            raise

    def send_keys(self, locator, key, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)) \
                .send_keys(key)
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            self.screenshot()
            raise

    def new_tab_is_opened(self, timeout=10):
        try:
            handles = self.driver.window_handles
            return WebDriverWait(self.driver, timeout).until(EC.new_window_is_opened(handles))
        except (InvalidSwitchToTargetException, NoSuchWindowException, TimeoutException):
            self.screenshot()
            raise

    def switch_to_tab(self, tab):
        try:
            tab1 = self.driver.window_handles[tab]
            self.driver.switch_to.window(tab1)
        except (InvalidSwitchToTargetException, NoSuchWindowException, TimeoutException):
            self.screenshot()
            raise

    def close_tab(self):
        try:
            tab0 = self.driver.window_handles[0]
            self.driver.close()
            self.driver.switch_to.window(tab0)
        except (InvalidSwitchToTargetException, NoSuchWindowException, TimeoutException):
            self.screenshot()
            raise

    def contains(self, locator, timeout=10):
        try:
            web_element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            value = web_element.text
            return value
        except (NoSuchElementException, AssertionError, TimeoutException):
            self.screenshot()
            raise

    def assert_text(self, locator, text, timeout=10):
        try:
            web_element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            value = web_element.text
            assert str(value) == str(text)
        except (NoSuchElementException, AssertionError, TimeoutException):
            self.screenshot()
            raise

    def contains_text(self, locator, attribute, text, timeout=10):
        try:
            web_element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            value = web_element.get_attribute(attribute)
            assert str(text) in str(value)
        except (NoSuchElementException, AssertionError, TimeoutException):
            self.screenshot()
            raise

    def scroll_to(self, locator):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", locator)
        except (NoSuchElementException, TimeoutException):
            self.screenshot()
            raise

    def get_title(self, title) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(title))
            return self.driver.title
        except Exception:
            self.screenshot()
            raise

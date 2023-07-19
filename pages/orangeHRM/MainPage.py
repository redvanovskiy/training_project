from base.base import Base
from selenium.webdriver.common.by import By


class MainPage(Base):
    _SEARCH_FIELD = (By.CSS_SELECTOR, "[placeholder='Search']")
    _ADMIN_BUTTON = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(1)")
    _ADMIN_BUTTON_ACTIVE = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(1) .active")
    _PIM_BUTTON = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(2)")
    _LEAVE_BUTTON = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(3)")
    _TIME_BUTTON = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(4)")
    _RECRUITMENT_BUTTON = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(5)")
    _MY_INFO_BUTTON = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(6)")
    _PERFORMANCE_BUTTON = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(7)")
    _DASHBOARD_BUTTON = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(8)")
    _DASHBOARD_BUTTON_ACTIVE = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(8) .active")
    _DIRECTORY_BUTTON = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(9)")
    _MAINTENANCE_BUTTON = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(10)")
    _CLAIM_BUTTON = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(11)")
    _BUZZ_BUTTON = (By.CSS_SELECTOR, ".oxd-main-menu li:nth-of-type(12)")


    def __init__(self, driver):
        super().__init__(driver)


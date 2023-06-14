import json
import pytest
import os
import base.utils

from extensions.driver_factory import DriverFactory

CURRENT_DIR = os.path.dirname(__file__)
CONFIG_PATH = f"{CURRENT_DIR}/config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["local", "remote"]
HOST = base.utils.HOST


@pytest.fixture(scope='session')
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


@pytest.fixture(scope="session")
def browser_setup(config):
    if "browser" not in config:
        raise Exception('The config file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]


@pytest.fixture(scope='session')
def wait_time_setup(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def url_setup():
    return HOST


@pytest.fixture(scope='class', autouse=True)
def setup(request, config):
    driver = DriverFactory.get_driver(config)
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    yield
    driver.delete_all_cookies()
    driver.quit()

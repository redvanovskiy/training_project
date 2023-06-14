import os

# --- ENV URL ---
HOST = os.getenv('BASE_URL', "https://www.facebook.com")

# --- SELENIUM HUB ---
SELENIUM_HUB_HOST = 'selenium-hub'
SELENIUM_HUB_PORT = os.getenv('SELENIUM_HUB_PORT', '4444')
SELENIUM_HUB_URL = 'http://' + SELENIUM_HUB_HOST + ":" + SELENIUM_HUB_PORT
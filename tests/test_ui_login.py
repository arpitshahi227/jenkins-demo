from pages.login_page import LoginPage
from utils.config import BASE_UI_URL

def test_valid_login(driver):
    login = LoginPage(driver)
    login.load(BASE_UI_URL)
    login.login("Admin", "admin123")
    assert "dashboard" in driver.current_url.lower()

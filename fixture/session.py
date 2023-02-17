from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.driver
        wd.get("http://localhost/addressbook")
        wd.set_window_size(1252, 714)

    def login(self, username, password):
        wd = self.app.driver
        self.open_home_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "Logout").click()

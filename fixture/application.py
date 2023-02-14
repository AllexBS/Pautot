from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.driver
        wd.get("http://localhost/addressbook/")
        wd.set_window_size(1252, 714)

    def destroy(self):
        self.driver.quit()

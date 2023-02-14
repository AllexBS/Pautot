from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.driver
        wd.get("http://localhost/addressbook/")
        wd.set_window_size(1252, 714)

    def open_group_page(self):
        wd = self.driver
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        wd = self.driver
        self.open_group_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group forms
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.driver
        wd.find_element(By.LINK_TEXT, "group page").click()

    def destroy(self):
        self.driver.quit()

# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False}, firefox_binary="C:/Software-testing/Mozilla Firefox/firefox.exe")
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def add_new_contact(self, wd):
        # add new contact
        wd.find_element_by_link_text("add new").click()

    def fill_the_field_of_firstname(self, wd):
        # fill the field of firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("fdsdf")

    def fill_the_field_of_lastname(self, wd):
        # fill the field of lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("dsffds")

    def fill_the_field_of_address(self, wd):
        # fill the field of address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("sdfdfs")

    def submit_the_information(self, wd):
        # submit the information
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_homepage(self, wd):
        # return to homepage
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()
        
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.add_new_contact(wd)
        self.fill_the_field_of_firstname(wd)
        self.fill_the_field_of_lastname(wd)
        self.fill_the_field_of_address(wd)
        self.submit_the_information(wd)
        self.return_to_homepage(wd)
        self.logout(wd)


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time



class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\tmoskvina\Downloads\geckodriver-v0.21.0-win64 (1)\geckodriver')
        self.wd.implicitly_wait(30)

    def test_create_new_pp(self):
        wd = self.wd
        self.open_home_page(wd)
        self.log_in(wd)
        self.open_pain_points_tab(wd)
        self.create_new_pp(wd)
        self.log_out(wd)

    def open_home_page(self):
        # open home page
        wd = self.wd
        wd.get("http://painpoint.ntrlab.ru/Auth/SignIn")

    def log_out(self):
        # log out
        wd = self.wd
        time.sleep(3)
        wd.find_element_by_id("myProfile").click()
        wd.find_element_by_link_text("Log Out").click()

    def create_new_pp(self, description="test auto"):
        wd = self.wd
        # create new pain point
        wd.find_element_by_id("add").click()
        # Choose Category
        time.sleep(1)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[2]/following::span[5]").click()
        wd.find_element_by_xpath("//ul[@id='newCategory_listbox']/li").click()
        time.sleep(1)
        # Choose Tags
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[2]/following::div[2]").click()
        time.sleep(1)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Any Tag'])[4]/following::li[1]").click()
        time.sleep(3)
        wd.find_element_by_id("newDescription").click()
        wd.find_element_by_id("newDescription").clear()
        wd.find_element_by_id("newDescription").send_keys("%s" % description)
        #change value of slider
        wd.find_element_by_css_selector("div.k-slider-track").click()
        wd.find_element_by_id("savePainPoint").click()

    def open_pain_points_tab(self):
        wd = self.wd
        # open pain points tab
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Dashboard'])[1]/following::span[1]").click()

    def log_in(self):
        wd = self.wd
        # log in
        wd.find_element_by_id("Email").clear()
        wd.find_element_by_id("Email").send_keys("user@user.user")
        wd.find_element_by_id("Password").clear()
        wd.find_element_by_id("Password").send_keys("123a45=A")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::input[2]").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()

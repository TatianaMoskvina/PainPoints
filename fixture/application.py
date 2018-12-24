from selenium import webdriver
import  time
import pytest
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\tmoskvina\Downloads\geckodriver-v0.21.0-win64 (1)\geckodriver')
        self.wd.implicitly_wait(40)
        self.session = SessionHelper(self)

    def invite_user(self, email):
        wd = self.wd
        wd.find_element_by_id("inviteUser").click()
        wd.find_element_by_id("emailField").clear()
        wd.find_element_by_id("emailField").send_keys("%s" % email)
        time.sleep(1)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='If you want to add a new CompanyOwner, leave it blank'])[1]/following::span[5]").click()
        time.sleep(1)
        wd.find_element_by_xpath("//ul[@id='companyField_listbox']/li[2]").click()
        time.sleep(1)
        wd.find_element_by_id("inviteBtn").click()


    def invite_new_co(self, email):
        # invite user
        wd = self.wd
        wd.find_element_by_id("inviteUser").click()
        wd.find_element_by_id("emailField").click()
        wd.find_element_by_id("emailField").clear()
        # submit invite
        wd.find_element_by_id("emailField").send_keys("%s" % email)
        wd.find_element_by_id("inviteBtn").click()

    def open_users_tab(self):
        wd = self.wd
        # open pain points page
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Pain Points'])[1]/following::span[1]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://painpoint.ntrlab.ru/Auth/SignIn")



    def destroy(self):
        self.wd.quit()
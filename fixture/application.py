from selenium import webdriver
import  time
import pytest
from fixture.session import SessionHelper
from fixture.users import UserHelper
from fixture.pp import PainPointsHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\tmoskvina\Downloads\geckodriver-v0.21.0-win64 (1)\geckodriver')
        self.wd.implicitly_wait(40)
        self.session = SessionHelper(self)
        self.user = UserHelper(self)
        self.pp = PainPointsHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://painpoint.ntrlab.ru/Auth/SignIn")



    def destroy(self):
        self.wd.quit()
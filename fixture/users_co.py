import  time

class UserCOHelper:

    def __init__(self, app):
        self.app = app

    def invite_user(self, email):
        wd = self.app.wd
        wd.find_element_by_id("activeInviteUserBtn").click()
        wd.find_element_by_id("emailField").clear()
        wd.find_element_by_id("emailField").send_keys("%s" % email)
        time.sleep(1)
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='If you want to add a new CompanyOwner, leave it blank'])[1]/following::span[5]").click()
        time.sleep(1)
        wd.find_element_by_xpath("//ul[@id='companyField_listbox']/li[2]").click()
        time.sleep(1)
        wd.find_element_by_id("inviteBtn").click()


    def invite_new_co(self, email):
        # invite user
        wd = self.app.wd
        wd.find_element_by_id("activeInviteUserBtn").click()
        wd.find_element_by_id("emailField").click()
        wd.find_element_by_id("emailField").clear()
        # submit invite
        wd.find_element_by_id("emailField").send_keys("%s" % email)
        wd.find_element_by_id("inviteBtn").click()

    def open_users_tab(self):
        wd = self.app.wd
        # open pain points page
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Pain Points'])[1]/following::span[1]").click()
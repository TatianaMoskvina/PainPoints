import  time

class UserCOHelper:

    def __init__(self, app):
        self.app = app

    def invite_user(self, email):
        wd = self.app.wd
        wd.find_element_by_id("activeInviteUserBtn").click()
        wd.find_element_by_id("activeEmailField").clear()
        wd.find_element_by_id("activeEmailField").send_keys("%s" % email)
        time.sleep(1)
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='If you want to add a new CompanyOwner, leave it blank'])[1]/following::span[5]").click()
        time.sleep(1)
        wd.find_element_by_xpath("//ul[@id='activeCompanyField_listbox']/li[2]").click()
        time.sleep(1)
        wd.find_element_by_id("activeYesInviteBtn").click()


    def delete_user(self):
        wd = self.app.wd
        self.open_users_tab()
        if wd.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='First Name'])[1]/following::th[1]") == 'Toster':
            wd.find_element_by_id("deleteBtn_f59317e2-6687-4c85-8bf8-f36f708186d2").click()
            wd.find_element_by_id("activeYesDeleteBtn").click()
        else: pass



    def invite_new_co(self, email):
        # invite user
        wd = self.app.wd
        wd.find_element_by_id("activeInviteUserBtn").click()
        wd.find_element_by_id("activeEmailField").click()
        wd.find_element_by_id("activeEmailField").clear()
        # submit invite
        wd.find_element_by_id("activeEmailField").send_keys("%s" % email)
        wd.find_element_by_id("activeYesInviteBtn").click()

    def open_users_tab(self):
        wd = self.app.wd
        # open pain points page
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Pain Points'])[1]/following::span[1]").click()


    def edit_profile(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='User Profile'])[1]/following::button[1]").click()
        wd.find_element_by_id("FirstName").clear()
        wd.find_element_by_id("FirstName").send_keys("Tatiana auto edit")
        wd.find_element_by_id("SecondName").clear()
        wd.find_element_by_id("SecondName").send_keys("user auto edit")
        wd.find_element_by_id("Country").clear()
        wd.find_element_by_id("Country").send_keys("Russia edit")
        wd.find_element_by_id("City").clear()
        wd.find_element_by_id("City").send_keys("Tomsk edit")
        wd.find_element_by_id("Zip").clear()
        wd.find_element_by_id("Zip").send_keys("123456789")
        wd.find_element_by_name("BusinessUnitId_input").clear()
        wd.find_element_by_name("BusinessUnitId_input").send_keys("control center")
        #save edition
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='User Profile'])[1]/following::button[1]").click()

    def open_users_page(self):
        wd = self.app.wd
        wd.find_element_by_id("myProfile").click()
        wd.find_element_by_link_text("Profile").click()

    def change_password(self):
        wd = self.app.wd
        wd.find_element_by_id("changePasswordBtn").click()
        wd.find_element_by_id("oldPassword").clear()
        wd.find_element_by_id("oldPassword").send_keys("123a45=A")
        wd.find_element_by_id("newPassword").clear()
        wd.find_element_by_id("newPassword").send_keys("123a45=A")
        wd.find_element_by_id("confirmPassword").clear()
        wd.find_element_by_id("confirmPassword").send_keys("123a45=A")
        wd.find_element_by_id("SaveBtn").click()
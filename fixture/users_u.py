class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_users_page(self):
        wd = self.app.wd
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

    def change_password(self):
        wd = self.app.wd
        wd.find_element_by_id("changePasswordBtn").click()
        wd.find_element_by_id("oldPassword").clear()
        wd.find_element_by_id("oldPassword").send_keys("Qq!123")
        wd.find_element_by_id("newPassword").clear()
        wd.find_element_by_id("newPassword").send_keys("Qq!123")
        wd.find_element_by_id("confirmPassword").clear()
        wd.find_element_by_id("confirmPassword").send_keys("Qq!123")
        wd.find_element_by_id("SaveBtn").click()





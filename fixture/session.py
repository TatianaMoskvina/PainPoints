

class SessionHelper:

    def __init__(self, app):
        self.app = app



    def log_out(self):
        # log out
        wd = self.app.wd
        wd.find_element_by_id("myProfile").click()
        wd.find_element_by_link_text("Log Out").click()


    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.log_out()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elemens_by_link_text("myProfile")) > 0

    def ensure_log_in(self, username):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.log_out()


    def as_logged_in_as(self):
        wd = self.app.wd
        username_login = wd.find_element_by_css_selector("div.name").text
        mass_of_username  = username_login.split(' ')
        for i in mass_of_username:
            if i == 'CompanyOwner)':
                return i
        return i == "CompanyOwner)"


    def log_in(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("Email").clear()
        wd.find_element_by_id("Email").send_keys("%s" % username)
        wd.find_element_by_id("Password").clear()
        wd.find_element_by_id("Password").send_keys("%s" % password)
        wd.find_element_by_xpath( "(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::input[2]").click()


class SessionHelper:

    def __init__(self, app):
        self.app = app



    def log_out(self):
        # log out
        wd = self.app.wd
        wd.find_element_by_id("myProfile").click()
        wd.find_element_by_link_text("Log Out").click()


    def log_in(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("Email").clear()
        wd.find_element_by_id("Email").send_keys("%s" % username)
        wd.find_element_by_id("Password").clear()
        wd.find_element_by_id("Password").send_keys("%s" % password)
        wd.find_element_by_xpath( "(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::input[2]").click()
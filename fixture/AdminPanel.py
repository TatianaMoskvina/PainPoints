import  time

class AdminPanelHelper:

    def __init__(self, app):
        self.app = app

    def open_admin_panel_tab(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[4]/a/span").click()

    def create_category(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Admin panel'])[1]/following::span[2]").click()
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='There you can manage dictionaries'])[1]/following::span[1]").click()
        wd.find_element_by_id("newCategoryFld").click()
        wd.find_element_by_id("newCategoryFld").clear()
        wd.find_element_by_id("newCategoryFld").send_keys("Auto test category")
        wd.find_element_by_id("addBtn").click()

    def edit_category(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Auto test category'])[1]/following::input[1]").click()
        time.sleep(1)
        wd.find_element_by_xpath("//input[@id='editCategoryFld']").click()
        wd.find_element_by_id("editCategoryFld").clear()
        wd.find_element_by_id("editCategoryFld").send_keys("Auto test category edit")
        wd.find_element_by_id("editBtn").click()


    def delete_category(self):
        wd = self.app.wd
        time.sleep(2)
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Name'])[1]/following::input[2]").click()
        time.sleep(2)
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Delete category'])[1]/following::input[2]").click()



import  time

class PainPointsHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        # open home page
        wd = self.app.wd
        wd.get("http://painpoint.ntrlab.ru/Auth/SignIn")


    def create_new_pp(self, description="test auto"):
        wd = self.app.wd
        # create new pain point
        wd.find_element_by_id("add").click()
        # Choose Category
        time.sleep(1)
        wd.find_element_by_xpath( "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[2]/following::span[5]").click()
        wd.find_element_by_xpath("//ul[@id='newCategory_listbox']/li").click()
        time.sleep(1)
        # Choose Tags
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[2]/following::div[2]").click()
        time.sleep(1)
        wd.find_element_by_xpath( "(.//*[normalize-space(text()) and normalize-space(.)='Any Tag'])[4]/following::li[1]").click()
        time.sleep(3)
        wd.find_element_by_id("newDescription").click()
        wd.find_element_by_id("newDescription").clear()
        wd.find_element_by_id("newDescription").send_keys("%s" % description)
        # change value of slider
        wd.find_element_by_css_selector("div.k-slider-track").click()
        wd.find_element_by_id("savePainPoint").click()


    def create_several_pp(self, description="test auto create several pp"):
        wd = self.app.wd
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
        # change value of slider
        wd.find_element_by_css_selector("div.k-slider-track").click()

        # save and add another
        wd.find_element_by_id("addAnother").click()
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
        # change value of slider
        wd.find_element_by_css_selector("div.k-slider-track").click()
        wd.find_element_by_id("savePainPoint").click()

    def open_pain_points_tab(self):
        wd = self.app.wd
        # open pain points tab
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Dashboard'])[1]/following::span[1]").click()

    def put_like(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Likes'])[1]/following::td[2]").click()
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Priority'])[3]/following::div[2]").click()
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Detailed information'])[1]/following::a[1]").click()


    def add_comment(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Likes'])[1]/following::td[2]").click()
        wd.find_element_by_id("new-comment").click()
        wd.find_element_by_id("new-comment").clear()
        wd.find_element_by_id("new-comment").send_keys("comment")
        wd.find_element_by_id("addComment").click()
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Detailed information'])[1]/following::a[1]").click()
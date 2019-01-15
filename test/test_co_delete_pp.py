import time


def test_delete_new_pp(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    app.pp.open_pain_points_tab()
    #if app.pp.count() == 0: this feature has been deleted
        #app.pp.create_new_pp()
        #time.sleep(1)
    app.pp.delete_pp()
    time.sleep(1)
    app.session.log_out()
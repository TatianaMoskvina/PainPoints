import time


def test_create_new_pp_CO(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    app.pp.open_pain_points_tab()
    #app.pp.create_new_pp_CO() this feature has been deleted
    time.sleep(1)
    app.session.log_out()

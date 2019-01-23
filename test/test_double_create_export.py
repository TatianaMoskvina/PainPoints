import time


def test_create_several_pp(app):
    app.open_home_page()
    app.session.log_in(username="user@user.user", password="123a45=A")
    app.pp.open_pain_points_tab()
    app.pp.create_several_pp()
    time.sleep(3)
    app.pp.create_new_pp()
    time.sleep(1)
    app.session.log_out()


def test_export_pp(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    app.pp.export_pp()
    time.sleep(2)
    app.session.log_out()

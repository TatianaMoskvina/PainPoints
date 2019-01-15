import time


def test_change_password(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    app.userCO.open_users_page()
    app.userCO.change_password()
    time.sleep(2)
    app.session.log_out()
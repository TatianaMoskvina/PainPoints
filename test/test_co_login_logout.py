import time

def test_login_logout(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    time.sleep(2)
    app.session.log_out()
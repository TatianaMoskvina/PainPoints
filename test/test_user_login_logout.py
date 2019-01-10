import time

def test_login_logout(app):
    app.open_home_page()
    app.session.log_in(username="tmoskvina@sinergo.ru", password="Qq!123")
    time.sleep(2)
    app.session.log_out()
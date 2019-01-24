import time

def test_delete_user(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    #app.session.ensure_log_in()
    time.sleep(2)
    app.userCO.delete_user()
    time.sleep(2)
    app.session.log_out()


def test_restore_user(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    time.sleep(2)
    app.userCO.restore_user()
    time.sleep(2)
    app.session.log_out()



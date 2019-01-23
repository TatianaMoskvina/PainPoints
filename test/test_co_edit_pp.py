import time


def test_edit_pp(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    app.pp.edit_pp()
    time.sleep(1)
    app.session.log_out()

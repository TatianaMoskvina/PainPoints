
import time


def test_user_edit_profile(app):
    app.open_home_page()
    app.session.log_in(username="tmoskvina@sinergo.ru", password="Qq!123")
    app.user.open_users_page()
    app.user.edit_profile()
    time.sleep(2)
    app.session.log_out()
from fixture.application import Application
import time
import pytest


def test_add_comment(app):
    app.open_home_page()
    app.session.log_in(username="tmoskvina@sinergo.ru", password="Qq!123")
    app.pp.open_pain_points_tab()
    time.sleep(1)
    #app.pp.put_like()
    app.pp.add_comment()
    time.sleep(1)
    app.session.log_out()
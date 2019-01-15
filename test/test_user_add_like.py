import time
import pytest


def test_add_like(app):
    app.open_home_page()
    app.session.log_in(username="tmoskvina@sinergo.ru", password="Qq!123")
    app.pp.open_pain_points_tab()
    time.sleep(1)
    #add like
    app.pp.add_like()
    time.sleep(1)
    #remove like
    #app.pp.add_like()
    time.sleep(1)
    app.session.log_out()
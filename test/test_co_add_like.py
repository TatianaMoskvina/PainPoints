import time
import pytest


def test_add_like(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    app.pp.open_pain_points_tab()
    time.sleep(1)
    #add like
    app.pp.add_like()
    time.sleep(1)
    #remove like
    #app.pp.add_like()
    time.sleep(1)
    app.session.log_out()

def test_remove_like(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    app.pp.open_pain_points_tab()
    time.sleep(1)
    #add like
    app.pp.add_like()
    time.sleep(1)
    #remove like
    #app.pp.add_like()
    time.sleep(1)
    app.session.log_out()
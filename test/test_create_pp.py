# -*- coding: utf-8 -*-
from fixture.application import Application
import time
import pytest



@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_new_pp(app):
    app.open_home_page()
    app.session.log_in(username="user@user.user", password="123a45=A")
    app.pp.open_pain_points_tab()
    app.pp.create_new_pp()
    time.sleep(1)
    app.session.log_out()




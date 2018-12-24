# -*- coding: utf-8 -*-

from fixture.application import Application
import time
import pytest

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_invite_new_user(app):
    app.open_home_page()
    app.session.log_in(username="po@po.po", password="123a45=A")
    app.open_users_tab()
    app.invite_user("tmoskvina+22@sinergo.ru")
    time.sleep(1)
    app.session.log_out()

def test_invite_new_co(app):
    app.open_home_page()
    app.session.log_in(username="po@po.po", password="123a45=A")
    app.open_users_tab()
    app.invite_new_co(email="tmoskvina+11@sinergo.ru")
    time.sleep(1)
    app.session.log_out()


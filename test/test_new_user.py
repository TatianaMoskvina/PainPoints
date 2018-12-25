# -*- coding: utf-8 -*-


import time



def test_invite_new_user(app):
    app.open_home_page()
    app.session.log_in(username="po@po.po", password="123a45=A")
    app.userCO.open_users_tab()
    app.userCO.invite_user("tmoskvina+22@sinergo.ru")
    time.sleep(1)
    app.session.log_out()

def test_invite_new_co(app):
    app.open_home_page()
    app.session.log_in(username="po@po.po", password="123a45=A")
    app.userCO.open_users_tab()
    app.userCO.invite_new_co(email="tmoskvina+11@sinergo.ru")
    time.sleep(1)
    app.session.log_out()


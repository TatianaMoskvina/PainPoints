# -*- coding: utf-8 -*-

import time


def test_create_new_pp(app):
    app.open_home_page()
    app.session.log_in(username="user@user.user", password="123a45=A")
    app.pp.open_pain_points_tab()
    app.pp.create_new_pp()
    time.sleep(1)
    app.session.log_out()




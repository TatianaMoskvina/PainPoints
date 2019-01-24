import time


def test_create_category(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    app.AdPan.open_admin_panel_tab()
    app.AdPan.create_category()
    time.sleep(1)
    app.session.log_out()


def test_edit_category(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    app.AdPan.open_admin_panel_tab()
    app.AdPan.edit_category()
    time.sleep(1)
    app.session.log_out()


def test_delete_category(app):
    app.open_home_page()
    app.session.log_in(username="co@co.co", password="123a45=A")
    app.AdPan.open_admin_panel_tab()
    app.AdPan.delete_category()
    time.sleep(1)
    app.session.log_out()
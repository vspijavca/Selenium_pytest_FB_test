from FB_Pages import SearchHelper

def test_fb_log(browser):
    fb_main_page = SearchHelper(browser)
    fb_main_page.go_to_site()
    fb_main_page.enter_email("asdfdg@gmail.com")
    fb_main_page.enter_passw("sdfsgfdgh")
    fb_main_page.click_on_the_enter_button()
    elements = fb_main_page.check_login()
    assert "Электронный" and "Зарегистрируйте" in elements
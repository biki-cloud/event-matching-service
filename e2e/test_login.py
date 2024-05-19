from playwright.sync_api import Playwright, expect, sync_playwright


def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/events/")
    page.get_by_role("link", name="").click()
    page.get_by_role("button", name="").click()
    page.get_by_role("link", name="Login", exact=True).click()
    page.get_by_placeholder("メールアドレス").click()
    page.get_by_placeholder("メールアドレス").fill("organizer1@example.com")
    page.get_by_placeholder("パスワード").click()
    page.get_by_placeholder("パスワード").fill("password")

    # "ログイン" ボタンが存在することを確認
    login_button = page.get_by_role("button", name="ログイン")
    expect(login_button).to_be_visible()
    page.get_by_role("button", name="ログイン").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_login(playwright)

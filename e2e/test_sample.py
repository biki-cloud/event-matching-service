from playwright.sync_api import Playwright, sync_playwright


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/")
    page.goto("http://127.0.0.1:8000/events/")
    page.get_by_role("button", name="").click()
    page.get_by_role("link", name=" No login").click()
    page.get_by_role("link", name="Login", exact=True).click()
    page.get_by_placeholder("メールアドレス").click()
    page.get_by_placeholder("メールアドレス").fill("organizer1@example.com")
    page.get_by_placeholder("パスワード").click()
    page.get_by_placeholder("パスワード").fill("password")
    page.get_by_role("button", name="ログイン").click()
    page.get_by_text("ユーザー organizer1 としてログインしました。").click()
    page.get_by_role("link", name=" organizer1").click()
    page.get_by_role("link", name=" organizer1").click()
    page.get_by_role("link", name=" organizer1").click()
    page.get_by_role("link", name=" organizer1").click()
    page.get_by_role("link", name=" organizer1").click()
    page.get_by_role("link", name=" organizer1").click()
    page.get_by_role("link", name=" organizer1").click()
    page.get_by_role("link", name="新規作成").click()
    page.get_by_label("Name:").click()
    page.get_by_label("Name:").fill("fjaojfoajofjoaf")
    page.get_by_role("button", name="保存").click()
    page.get_by_role("link", name="新規作成").click()
    page.get_by_label("Name:").click()
    page.get_by_label("Name:").fill("fafafaffa")
    page.get_by_label("Status:").select_option("published")
    page.get_by_role("button", name="保存").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)

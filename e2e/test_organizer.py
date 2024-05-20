import allure
from playwright.sync_api import Page


@allure.title("GitHubでYusukeIwakiのページを確認する")
def test_signup_organizer(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/events/")

    # ログインページへ遷移
    # IDを使ってボタンをクリック
    page.click("#auth_link")
    # page.get_by_role("button", name="").click()
    # page.get_by_role("link", name=" No login").click()
    # page.get_by_role("link", name="Register").click()

    # # メールアドレス入力
    # page.get_by_placeholder("メールアドレス").click()
    # page.get_by_placeholder("メールアドレス").fill("organizer3@example.com")
    # page.get_by_placeholder("パスワード").click()
    # page.get_by_placeholder("パスワード").fill("Org123@#")
    # page.get_by_role("button", name="ユーザー登録").click()

    # # ログイン成功メッセージを確認
    # success_message = page.get_by_text("ユーザー organizer3 としてログインしました。")
    # expect(success_message).to_be_visible()

    # # イベント主催者登録メッセージを確認
    # organizer_message = page.get_by_text("イベント主催者として登録しました")
    # expect(organizer_message).to_be_visible()

    # # イベントタイプ(published)でイベント新規作成
    # page.get_by_role("link", name="新規作成").click()
    # page.get_by_label("Name:").click()
    # page.get_by_label("Name:").fill("ffffff")
    # page.get_by_label("Status:").select_option("published")
    # page.get_by_role("button", name="保存").click()
    # # イベント一覧ページに表示できているか
    # expect(page.get_by_role("cell", name="ffffff")).to_be_visible()

from playwright.sync_api import Page


def test_access(page: Page):
    page.goto("http://127.0.0.1:8000/events/")

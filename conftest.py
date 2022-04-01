import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Language"
    )


@pytest.fixture
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.implicitly_wait(15)
    yield browser    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

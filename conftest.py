import pytest
from selenium import webdriver

# Фикстура финализатор
# После завершения теста, который вызывал фикстуру,
# выполнение фикстуры продолжится со строки, следующей за строкой со словом yield
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("/Users/zaytsev/PycharmProjects/Unit_28_Final_SF/chromedriver")
    yield browser
    print("\nquit browser..")
    browser.quit()


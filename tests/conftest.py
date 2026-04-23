# Фикстура — это предустановленные данные или состояние системы,
# необходимые для тестирования. Она помогает создать стабильную среду для
# выполнения тестов, обеспечивая повторяемость и изоляцию.
# Фикстуры могут располагаться как внутри тестового файла, так и в отдельном файле (conftest.py).
# Для назначения фикстур используется декоратор "@pytest.fixture".
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    # Код до yeld выполняется перед тестом (как @Before в Java)
    yield driver

    # Код после yeld выполняется после теста (как @After в Java)
    driver.quit()
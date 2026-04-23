from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Это плохой тест чисто для примера
def main():
    print("Инициализация браузера")

    #Настройка опций (опционально)
    options = webdriver.ChromeOptions()

    #options.add_argument('--headless')

    # Инициализация драйвера с помощью менеджера. До версии 4.10 нужно было драйвер браузера скачивать.
    # И фреймворк WebDriverManager помогал скачивать
    # Начиная с версии 4.10 Selenium сам занимается этими делами.

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Открытие страницы
        driver.get("https://www.python.org")

        # Поиск элемента, очистка поля, ввод текста
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys("Selenium")

        # Проверка заголовка
        assert "Python" in driver.title
        print(f"Заголовок страницыm {driver.title}")

    except Exception as e:
        print(f"Произошла ощибка {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()



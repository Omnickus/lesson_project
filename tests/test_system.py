# Импорты для pytest
import pytest
import allure

from elements import Url_page
from src.object_system import System
from src.base.logger import log_decorator


@pytest.mark.system
class Test_system:

    @allure.description("Проверка полей на вкладке 'Система' на корректные данные")
    @allure.feature("Система")
    @allure.story("Проверка полей на вкладке 'Система' на корректные данные")
    @allure.step
    @pytest.mark.parametrize("name_test, path, test_data", System.param )
    def test_system_page_correct_tests(self, driver, name_test, path, test_data):
        driver.get(driver.url + Url_page.system_page)
        for i in test_data['correct_test']:
            @log_decorator
            def start():
                System(driver).object_system(name_test = name_test, path = path, text = i['text'], status = i['status'])
            start()

    @allure.description("Проверка полей на вкладке 'Система' на строковые данные")
    @allure.feature("Система")
    @allure.story("Проверка полей на вкладке 'Система' на строковые данные")
    @allure.step
    @pytest.mark.parametrize("name_test, path, test_data", System.param )
    def test_system_page_string_tests(self, driver, name_test, path, test_data):
        driver.get(driver.url + Url_page.system_page)
        for i in test_data['string']:
            @log_decorator
            def start():
                System(driver).object_system(name_test = name_test, path = path, text = i['text'], status = i['status'])
            start()

    @allure.description("Проверка полей на вкладке 'Система' на числовые данные")
    @allure.feature("Система")
    @allure.story("Проверка полей на вкладке 'Система' на числовые данные")
    @allure.step
    @pytest.mark.parametrize("name_test, path, test_data", System.param )
    def test_system_page_integer_tests(self, driver, name_test, path, test_data):
        driver.get(driver.url + Url_page.system_page)
        for i in test_data['integer']:
            @log_decorator
            def start():
                System(driver).object_system(name_test = name_test, path = path, text = i['text'], status = i['status'])
            start()

    @allure.description("Проверка полей на вкладке 'Система' с отсутствием данных")
    @allure.feature("Система")
    @allure.story("Проверка полей на вкладке 'Система' с отсутствием данных")
    @allure.step
    @pytest.mark.parametrize("name_test, path, test_data", System.param )
    def test_system_page_empty_tests(self, driver, name_test, path, test_data):
        driver.get(driver.url + Url_page.system_page)
        for i in test_data['empty']:
            @log_decorator
            def start():
                System(driver).object_system(name_test = name_test, path = path, text = i['text'], status = i['status'])
            start()

    @allure.description("Проверка полей на вкладке 'Система' на спец символы")
    @allure.feature("Система")
    @allure.story("Проверка полей на вкладке 'Система' на спец символы")
    @allure.step
    @pytest.mark.parametrize("name_test, path, test_data", System.param )
    def test_system_page_special_char_tests(self, driver, name_test, path, test_data):
        driver.get(driver.url + Url_page.system_page)
        for i in test_data['special_char']:
            @log_decorator
            def start():
                System(driver).object_system(name_test = name_test, path = path, text = i['text'], status = i['status'])
            start()



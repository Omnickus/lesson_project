# Импорты для pytest
import pytest
import allure
import config

from src.object_types_publications import Types_publications
from src.base.logger import Logger               # Логгер
from src.base.logger import log_decorator


@pytest.mark.types_publications
class Test_types_publications:

    @allure.description("Создание/Удаление типа публикации")
    @allure.feature("Типы публикаций")
    @allure.story("Создание/Удаление типа публикации")
    @allure.step
    @pytest.mark.parametrize("path, test_data", Types_publications.params_create_publications )
    def test_create_type_publications(self, driver, path, test_data):
        driver.get(driver.url + Types_publications._url)
        @log_decorator
        def start():
            Logger(f'{config.indicator_test_page} {Types_publications._report}').infolog
            Logger(f'{config.indicator_test_name} Создание нового типа публикации').infolog
            Logger(f'{config.indicator_test_param} Тестовые значения {test_data["test_data"]}').infolog
            name_publications = Types_publications(driver).create_publications(path, test_data)
            Types_publications(driver).delete_type_publications(name = name_publications)
        start()

    @allure.description("Создание/Редактирование/Удаление типа публикации")
    @allure.feature("Типы публикаций")
    @allure.story("Создание/Редактирование/Удаление типа публикации")
    @allure.step
    @pytest.mark.parametrize("path, test_data", Types_publications.params_create_publications )
    def test_edit_type_publications(self, driver, path, test_data):
        driver.get(driver.url + Types_publications._url)
        @log_decorator
        def start():
            Logger(f'{config.indicator_test_page} {Types_publications._report}').infolog
            Logger(f'{config.indicator_test_name} Редактирование нового типа публикации').infolog
            Logger(f'{config.indicator_test_param} Тестовые значения {Types_publications.params_edit_publications["test_data"]}').infolog
            name_publications = Types_publications(driver).create_publications(path = path, test_data = test_data)
            name_publications = Types_publications(driver).edit_type_publications(name = name_publications)
            Types_publications(driver).delete_type_publications(name = name_publications)
        start()


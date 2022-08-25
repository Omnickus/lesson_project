# Импорты для pytest
import pytest
import allure
import config

from src.object_places_publication import Places_publication
from src.base.logger import Logger               # Логгер
from src.base.logger import log_decorator


@pytest.mark.places_publication
class Test_places_publication:

    @allure.description("Создание/Редактирование/Удаление места публикации")
    @allure.feature("Места публикации")
    @allure.story("Создание/Редактирование/Удаление места публикации")
    @pytest.mark.parametrize('test_data', Places_publication.params_create_palace_publication)
    def test_create_place_publication(self, driver, test_data):
        @log_decorator
        def start():
            driver.get(driver.url + Places_publication._url)
            Logger(f'{config.indicator_test_page} {Places_publication._report}').infolog
            Logger(f'{config.indicator_test_name} Создание нового места публикации').infolog
            Logger(f'{config.indicator_test_param} Тестовое значение {test_data}').infolog
            name_new_publications = Places_publication(driver).create_new_place_publication(test_data)
        start()

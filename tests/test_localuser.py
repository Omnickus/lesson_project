# Импорты для pytest
import pytest
import allure

from src.object_localuser import Localuser

from src.base.logger import log_decorator
from src.base.logger import Logger
import config


@pytest.mark.localuser
class Test_localuser:

    @allure.description("Создание\Удаление локального пользователя")
    @allure.feature("Локальные пользователи")
    @allure.story("Создание\Удаление локального пользователя")
    @allure.step
    @pytest.mark.parametrize('test_name, path, test_data', Localuser.param_create_new_user)
    def test_creat_new_local_user(self, driver, test_name, path, test_data):
        @log_decorator
        def start():
            Logger(f'{config.indicator_test_page} {Localuser._report}').infolog
            Logger(f'{config.indicator_test_name} Создание локального пользователя').infolog
            Logger(f'{config.indicator_test_param} Тестовое значение {test_data}').infolog
            name_new_local_user = Localuser(driver).create_new_user(test_name, path, test_data)
            Localuser(driver=driver).del_localuser(text = name_new_local_user)
        start()


    @allure.description("Создание\Редактирование\Удаление локального пользователя")
    @allure.feature("Локальные пользователи")
    @allure.story("Создание\Редактирование\Удаление локального пользователя")
    @allure.step
    @pytest.mark.parametrize('test_name, path, test_data', Localuser.param_create_new_user)
    def test_edit_local_user(self, driver, test_name, path, test_data):
        @log_decorator
        def start():
            Logger(f'{config.indicator_test_page} {Localuser._report}').infolog
            Logger(f'{config.indicator_test_name} Редактирование локального пользователя').infolog
            Logger(f'{config.indicator_test_param} Тестовое значение {test_data}').infolog
            name_new_local_user = Localuser(driver).create_new_user(test_name, path, test_data)
            name_editing_local_user = Localuser(driver).edit_user(test_name, path, test_data)
            Localuser(driver=driver).del_localuser(text = name_editing_local_user)
        start()
        

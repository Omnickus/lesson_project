# Импорты для pytest
import pytest
import allure
from src.object_allowed_addresses import Allowed_addresses

from src.base.logger import log_decorator


@pytest.mark.allowed_addresses
class Test_allowed_addresses:

    @allure.description("Создание/Удаление разрешённого адреса")
    @allure.feature("Разрешённые адреса")
    @allure.story("Создание/Удаление разрешённого адреса")
    @pytest.mark.parametrize('test_name, path, test_data', Allowed_addresses.param_create_new_user)
    def test_creat_new_allowed_addresses(self, driver, test_name, path, test_data):
        @log_decorator
        def start():
            name_new_allowed_address = Allowed_addresses(driver).create_new_user(test_name, path, test_data)
            Allowed_addresses(driver = driver).del_allowed_address(text = name_new_allowed_address)
        start()


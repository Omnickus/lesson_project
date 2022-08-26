# Импорты для pytest
import pytest
import allure
from src.base.logger import log_decorator

from src.object_service_management import Service_management



@pytest.mark.service_management
class Test_service_management:
    
    @allure.description("Остановка сервиса")
    @allure.feature("Микросервисы")
    @allure.story("Остановка сервиса")
    @pytest.mark.parametrize("service", Service_management._one_service_at_a_time )
    def test_stop_services_at_a_time(self, driver, service):
        @log_decorator
        def start():
            Service_management(driver = driver).stop_services_at_a_time(service)
        start()

    @allure.description("Запуск сервиса")
    @allure.feature("Микросервисы")
    @allure.story("Запуск сервиса")
    @pytest.mark.parametrize("service", Service_management._one_service_at_a_time )
    def test_start_services_at_a_time(self, driver, service):
        @log_decorator
        def start():
            Service_management(driver = driver).start_services_at_a_time(service)
        start()
        


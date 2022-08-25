# Импорты для pytest
import pytest
import allure
from src.base.logger import log_decorator

from src.object_supply_routes import Supply_routes



@pytest.mark.supply_routes
class Test_supply_routes:
    

    @allure.description("Создание/Удаление маршрута публикации")
    @allure.feature("Маршруты")
    @allure.story("Создание/Удаление маршрута публикации")
    @allure.step
    def test_create_new_route(self, driver):
        for i in [1]:
            @log_decorator
            def start():
                name_new_route = Supply_routes(driver = driver).create_new_route()
                Supply_routes(driver = driver).del_route(text = name_new_route)
            start()

    @allure.description("Создание/Редактирование/Удаление маршрута публикации")
    @allure.feature("Маршруты")
    @allure.story("Создание/Редактирование/Удаление маршрута публикации")
    @allure.step
    def test_edit_route(self, driver):
        for i in [1]:
            @log_decorator
            def start():
                name_new_route = Supply_routes(driver = driver).create_new_route()
                name_editing_route = Supply_routes(driver = driver).edit_route(text = name_new_route)
                Supply_routes(driver = driver).del_route(text = name_editing_route)
            start()


    @allure.description("Выбор маршрутов")
    @allure.feature("Маршруты")
    @allure.story("Выбор маршрутов")
    @allure.step
    def test_route_selection(self, driver):
        for i in [1]:
            @log_decorator
            def start():
                Supply_routes(driver = driver).route_selection()
            start()




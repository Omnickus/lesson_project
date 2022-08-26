import config
from src.base.base_page import Base_page
import allure
from allure_commons.types import AttachmentType

# Импорт вспомогательных классов
from src.base.constructor import Find_element   
from src.base.constructor import Placeholder   
from src.base.constructor import Actions        
from src.base.logger import Logger            
from src.base.logger import log_decorator     


class Service_management(Base_page):

    __name = 'Класс для работы с элементами на странице "Управление сервисами"'
    _report = "Страница 'Управление сервисами'"
    _url = 'uta/admin/restartC'

    __path_status = '//*[@id="settings_service_modal"]'
    __text_status_start = 'Сервис успешно запущен'
    __text_status_stop = 'Сервис успешно остановлен'


    __start_all_services = '//*[@id="settings_start_all_button"]'
    __stop_all_services = '//*[@id="settings_stop_all_button"]'

    _one_service_at_a_time = [
        (
            {
                'start' : {
                    'test_name' : 'Запуск сервиса Антивирусная проверка',
                    'path' : '//*[@id="settings_start_antivir_button"]',
                    'status' : __text_status_start
                },
                'stop'  : {
                    'test_name' : 'Остановка сервиса Антивирусная проверка',
                    'path' : '//*[@id="settings_stop_antivir_button"]',
                    'status' : __text_status_stop
                }
            }
        ),(
            {
                'start' : {
                    'test_name' : 'Запуск сервиса Расчёт контрольных сумм',
                    'path' : '//*[@id="settings_start_calccrc_button"]',
                    'status' : __text_status_start
                },
                'stop'  : {
                    'test_name' : 'Остановка сервиса Расчёт контрольных сумм',
                    'path' : '//*[@id="settings_stop_calccrc_button"]',
                    'status' : __text_status_stop
                }
            }
        ),(
            {
                'start' : {
                    'test_name' : 'Запуск сервиса криптографическая обработка',
                    'path' : '//*[@id="settings_start_crypto_button"]',
                    'status' : __text_status_start
                },
                'stop'  : {
                    'test_name' : 'Остановка сервиса криптографическая обработка',
                    'path' : '//*[@id="settings_stop_crypto_button"]',
                    'status' : __text_status_stop
                }
            }
        ),(
            {
                'start' : {
                    'test_name' : 'Запуск сервиса почта',
                    'path' : '//*[@id="settings_start_mailer_button"]',
                    'status' : __text_status_start
                },
                'stop'  : {
                    'test_name' : 'Остановка сервиса почта',
                    'path' : '//*[@id="settings_stop_mailer_button"]',
                    'status' : __text_status_stop
                }
            }
        ),(
            {
                'start' : {
                    'test_name' : 'Запуск сервиса Публикация данных',
                    'path' : '//*[@id="settings_start_publisher_button"]',
                    'status' : __text_status_start
                },
                'stop'  : {
                    'test_name' : 'Остановка сервиса Публикация данных',
                    'path' : '//*[@id="settings_stop_publisher_button"]',
                    'status' : __text_status_stop
                }
            }
        ),(
            {
                'start' : {
                    'test_name' : 'Запуск сервиса Разархивирование',
                    'path' : '//*[@id="settings_start_unzip_button"]',
                    'status' : __text_status_start
                },
                'stop'  : {
                    'test_name' : 'Остановка сервиса Разархивирование',
                    'path' : '//*[@id="settings_stop_unzip_button"]',
                    'status' : __text_status_stop
                }
            }
        ),
    ]



    def stop_services_at_a_time(self, service):
        self._driver.get(self._driver.url + self._url)
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_page} {self._report}').infolog
        Logger(f'{config.indicator_test_name} {service["stop"]["test_name"]}').infolog
        Logger(f'{config.indicator_test_param} Тестовые значения {service["stop"]["test_name"]}').infolog

        el = Find_element(driver = self._driver, path = service['stop']['path'], wtime = 15).by_xpath_to_be_clickable_no_scroll
        el.click()
        Logger(f'{config.indicator_test_step} Нажал остановить сервис').infolog
        el = Find_element(driver = self._driver, path = self.__path_status, wtime = 15).by_xpath_to_be_visibility
        Logger(f'{config.indicator_test_step} Читаю сообщение').infolog
        if el.text != self.__text_status_stop:
            name_screen = self.save_screen_shot
            allure.attach(self._driver.get_screenshot_as_png(), name=name_screen, attachment_type=AttachmentType.PNG)
            Logger(f'{config.indicator_test_result_err} Сервис не остановлен').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            assert el.text == self.__text_status_stop
        else:
            Logger(f'{config.indicator_test_result_suc} Сервис остановлен').infolog
            assert el.text == self.__text_status_stop


    def start_services_at_a_time(self, service):
        self._driver.get(self._driver.url + self._url)
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_page} {self._report}').infolog
        Logger(f'{config.indicator_test_name} {service["start"]["test_name"]}').infolog
        Logger(f'{config.indicator_test_param} Тестовые значения {service["start"]["test_name"]}').infolog

        el = Find_element(driver = self._driver, path = service['start']['path'], wtime = 15).by_xpath_to_be_clickable_no_scroll
        el.click()
        Logger(f'{config.indicator_test_step} Нажал запустить сервис').infolog
        el = Find_element(driver = self._driver, path = self.__path_status, wtime = 15).by_xpath_to_be_visibility
        Logger(f'{config.indicator_test_step} Читаю сообщение').infolog
        if el.text != self.__text_status_start:
            name_screen = self.save_screen_shot
            allure.attach(self._driver.get_screenshot_as_png(), name=name_screen, attachment_type=AttachmentType.PNG)
            Logger(f'{config.indicator_test_result_err} Сервис не запустился').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            assert el.text == self.__text_status_start
        else:
            Logger(f'{config.indicator_test_result_suc} Сервис запустился').infolog
            assert el.text == self.__text_status_start

import config
from src.base.base_page import Base_page
import allure
from allure_commons.types import AttachmentType

# Импорт вспомогательных классов
from src.base.constructor import Find_element    # Поиск элементов
from src.base.constructor import Placeholder     # Взаимодействие с текстовыми полями, чек-боксами, радиокнопками и тд.
from src.base.constructor import Actions         # Разные действия
from src.base.logger import Logger               # Логгер
from src.base.logger import log_decorator        # Обёртка для логов

import random

class Supply_routes(Base_page):

    __name = 'Класс для работы с элементами на странице "Маршруты"'
    _report = "Страница 'Маршруты'"
    _url = 'uta/admin/path'

    _active = '//*[@id="menu-"]/div[3]/ul/li[1]'
    _not_active = '//*[@id="menu-"]/div[3]/ul/li[2]'

    _activa_choece = [_active, _not_active]

    _but_edit_when_edit = '/td[1]/div/button[1]'
    _but_del_when_edit = '/td[1]/div/button[2]'
    _but_save_when_edit = '/td[1]/div/button[1]'
    _but_cancel_when_edit = '/td[1]/div/button[2]'

    _button_when_create = {
        "_create_new_rout" : '//*[@id="tab-panel-tabpane-path"]/div[2]/div[1]/div[3]/div/div/span/button',
        "_name_route" : '//*[@id="tab-panel-tabpane-path"]/div[2]/div[2]/div/div/div/table/tbody/tr[2]/td[2]/div/div/input',
        "_get_data" : '//*[@id="tab-panel-tabpane-path"]/div[2]/div[2]/div/div/div/table/tbody/tr[2]/td[3]/div/div/div',
        "_crypt_work" : '//*[@id="tab-panel-tabpane-path"]/div[2]/div[2]/div/div/div/table/tbody/tr[2]/td[4]/div/div/div',
        "_zipper" : '//*[@id="tab-panel-tabpane-path"]/div[2]/div[2]/div/div/div/table/tbody/tr[2]/td[5]/div/div/div',
        "_antivirus_scaning" : '//*[@id="tab-panel-tabpane-path"]/div[2]/div[2]/div/div/div/table/tbody/tr[2]/td[6]/div/div/div',
        "_hash_sum" : '//*[@id="tab-panel-tabpane-path"]/div[2]/div[2]/div/div/div/table/tbody/tr[2]/td[7]/div/div/div',
        "_publictions" : '//*[@id="tab-panel-tabpane-path"]/div[2]/div[2]/div/div/div/table/tbody/tr[2]/td[8]/div/div/div',
        '_but_save' : '//*[@id="tab-panel-tabpane-path"]/div[2]/div[2]/div/div/div/table/tbody/tr[2]/td[1]/div/button[1]',
    }
    _button_when_edit = {
        "_route_name" : '/td[2]/div/div/input',
        "_route_get_data" : '/td[3]/div/div',
        "_route_crypt_work" : '/td[4]/div/div',
        "_route_zipper" : '/td[5]/div/div',
        "_route_antivirus_scaning" : '/td[6]/div/div',
        "_route_hash_sum" : '/td[7]/div/div',
        "_route_publictions" : '/td[8]/div/div',
    }

    # Для теста выбора маршрутов 
    choose_route = {
        'edit' : '//*[@id="tab-panel-tabpane-path"]/div[1]/div/div/div/div/table/tbody/tr/td[1]/div/button',
        'counter_params' : {
            'artifact_storage' : {
                'path' : '//*[@id="tab-panel-tabpane-path"]/div[1]/div/div/div/div/table/tbody/tr/td[2]/div/div/div',
                'name' : 'Хранилище артефактов',
                'check' : {
                    'path' : '//*[@id="tab-panel-tabpane-path"]/div[1]/div/div/div/div/table/tbody/tr/td[2]',
                    'meaning' : '',
                    'initial_values' : ''
                } 
            },
            'source_code_repository' : {
                'path' : '//*[@id="tab-panel-tabpane-path"]/div[1]/div/div/div/div/table/tbody/tr/td[3]/div/div/div',
                'name' : 'Хранилище исходного кода',
                'check' : {
                    'path' : '//*[@id="tab-panel-tabpane-path"]/div[1]/div/div/div/div/table/tbody/tr/td[3]',
                    'meaning' : '',
                    'initial_values' : ''
                }
            },
            'catalog' : { 
                'path' : '//*[@id="tab-panel-tabpane-path"]/div[1]/div/div/div/div/table/tbody/tr/td[4]/div/div/div',
                'name' : 'Каталог',
                'check' : {
                    'path' : '//*[@id="tab-panel-tabpane-path"]/div[1]/div/div/div/div/table/tbody/tr/td[4]',
                    'meaning' : '',
                    'initial_values' : ''
                }
            }
        },
        'menu_choose_route' : '//*[@id="menu-"]/div[3]/ul/li',
        'save_route' : '//*[@id="tab-panel-tabpane-path"]/div[1]/div/div/div/div/table/tbody/tr/td[1]/div/button[1]'
    }



    def create_new_route(self, flag = None):
        test_name_for_route = 'Selen_route' + str( Base_page().random_int(1000, 99000) )
        self._driver.get(self._driver.url + self._url)

        Logger(f'{config.indicator_test_page} {self._report}').infolog
        Logger(f'{config.indicator_test_name} Создание/Редактирование/Удаление маршрута').infolog
        Logger(f'{config.indicator_test_param} Тестовые значения: Название маршрута {test_name_for_route} и все микросервисы выбираются рандомно').infolog

        el = Find_element(driver = self._driver, path = self._button_when_create['_create_new_rout'], wtime = 10).by_xpath_to_be_clickable_no_scroll
        el.click()
        Logger(f'{config.indicator_test_step} Нажал создать новый маршрут').infolog
        
        el = Find_element(driver = self._driver, path = self._button_when_create['_name_route'], wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = test_name_for_route)
        Logger(f'{config.indicator_test_step} Ввёл имя').infolog

        el = Find_element(driver = self._driver, path = self._button_when_create['_get_data'], wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = random.choice(self._activa_choece), wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал получение данных').infolog

        el = Find_element(driver = self._driver, path = self._button_when_create['_crypt_work'], wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = random.choice(self._activa_choece), wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал криптографическую обработку').infolog

        el = Find_element(driver = self._driver, path = self._button_when_create['_zipper'], wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = random.choice(self._activa_choece), wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал разархивирование').infolog

        el = Find_element(driver = self._driver, path = self._button_when_create['_antivirus_scaning'], wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = random.choice(self._activa_choece), wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал антивирусную проверку').infolog

        el = Find_element(driver = self._driver, path = self._button_when_create['_hash_sum'], wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = random.choice(self._activa_choece), wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал проверку хэш суммы').infolog

        el = Find_element(driver = self._driver, path = self._button_when_create['_publictions'], wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = random.choice(self._activa_choece), wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал публикацию данных').infolog

        el = Find_element(driver = self._driver, path = self._button_when_create['_but_save'], wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Нажал сохранить').infolog
        self.time_out_animation

        self._driver.refresh()
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_step} Обновил страницу').infolog

        Logger(f'{config.indicator_test_step} Ищу созданный маршрут').infolog

        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = test_name_for_route)
        if dinamic_path == None:
            name_screen = self.save_screen_shot
            allure.attach(self._driver.get_screenshot_as_png(), name='screen_shot', attachment_type=AttachmentType.PNG)
            Logger(f'{config.indicator_test_result_err} Не удалось найти созданный маршрут').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            assert dinamic_path != None

        Logger(f'{config.indicator_test_result_suc} Созданный маршрут найден').infolog

        return test_name_for_route


    def edit_route(self, text = None):

        Logger(f'{config.indicator_test_step} Редактирую маршрут').infolog
        self.time_out_free
        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = text)
        el = Find_element(driver = self._driver, path = dinamic_path + self._but_edit_when_edit, wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation

        el = Find_element(driver = self._driver, path = dinamic_path + self._button_when_edit['_route_name'], wtime = 30).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        Placeholder(driver = self._driver).clear_place(el = el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = text)
        Logger(f'{config.indicator_test_step} Отредактировал имя').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._button_when_edit['_route_get_data'], wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = random.choice(self._activa_choece), wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал получение данных').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._button_when_edit['_route_crypt_work'], wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = random.choice(self._activa_choece), wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал криптографическую обработку').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._button_when_edit['_route_zipper'], wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = random.choice(self._activa_choece), wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал разархивирование').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._button_when_edit['_route_antivirus_scaning'], wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = random.choice(self._activa_choece), wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал антивирусную проверку').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._button_when_edit['_route_hash_sum'], wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = random.choice(self._activa_choece), wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал проверку хэш суммы').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._button_when_edit['_route_publictions'], wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = random.choice(self._activa_choece), wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал публикацию данных').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._but_save_when_edit, wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Нажал сохранить').infolog
        self.time_out_animation

        self._driver.refresh()
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_step} Обновил страницу').infolog

        Logger(f'{config.indicator_test_step} Ищу отредактированный маршрут').infolog

        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = text)
        if dinamic_path == None:
            name_screen = self.save_screen_shot
            allure.attach(self._driver.get_screenshot_as_png(), name='screen_shot', attachment_type=AttachmentType.PNG)
            Logger(f'{config.indicator_test_result_err} Не удалось найти отредактированный маршрут').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            assert dinamic_path != None

        Logger(f'{config.indicator_test_result_suc} Отредактированный маршрут найден').infolog

        return text


    def del_route(self, text = None, status_start = None):

        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = text)
        
        el = Find_element(driver = self._driver, path = dinamic_path + self._but_del_when_edit).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Нажал удалить маршрут').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._but_save_when_edit).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Нажал подтвердить удаление').infolog
        self.time_out_animation

        self._driver.refresh()
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_step} Обновил страницу').infolog

        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = text)
        if dinamic_path != None:
            name_screen = self.save_screen_shot
            allure.attach(self._driver.get_screenshot_as_png(), name='screen_shot', attachment_type=AttachmentType.PNG)
            Logger(f'{config.indicator_test_result_err} Не удалось удалить маршрут').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            assert dinamic_path == None

        Logger(f'{config.indicator_test_result_suc} Маршрут удалён').infolog


    def route_selection(self):
        self._driver.get(self._driver.url + self._url)

        Logger(f'{config.indicator_test_page} {self._report}').infolog
        Logger(f'{config.indicator_test_name} Выбор маршрутов').infolog
        Logger(f'{config.indicator_test_param} Тестовые значения: маршрут для каждого типа поставки выбирается случайно').infolog

        for i in self.choose_route['counter_params']:
            el = Find_element(driver = self._driver, path = self.choose_route['counter_params'][i]['check']['path'], wtime = 15).by_xpath_to_be_visibility_no_scroll
            self.choose_route['counter_params'][i]['check']['initial_values'] = el.text

        Logger(f'{config.indicator_test_step} Записал начальные значения').infolog

        el = Find_element(driver = self._driver, path = self.choose_route['edit'], wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).click_js(el)
        Logger(f'{config.indicator_test_step} Кликнул редактировать').infolog
        self.time_out_animation

        for param in self.choose_route['counter_params']:
            el = Find_element(driver = self._driver, path = self.choose_route['counter_params'][param]['path']).by_xpath_to_be_clickable_no_scroll
            Actions(driver = self._driver).actions_click(el)
            Logger(f'{config.indicator_test_step} Открыл выбор маршрутов для {self.choose_route["counter_params"][param]["name"]}').infolog
            self.time_out_animation

            el = Find_element(driver = self._driver, path = self.choose_route['menu_choose_route']).by_xpath_get_elements
            choose = self.random_int(1, len(el))
            el = Find_element(driver = self._driver, path = f'//*[@id="menu-"]/div[3]/ul/li[{str(choose)}]').by_xpath_to_be_visibility_no_scroll
            self.choose_route['counter_params'][param]['check']['meaning'] = el.text
            Actions(driver = self._driver).actions_click(el)
            Logger(f'{config.indicator_test_step} Выбрал маршрут').infolog
            self.time_out_animation

        el = Find_element(driver = self._driver, path = self.choose_route['save_route']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Logger(f'{config.indicator_test_step} Нажал сохранить').infolog
        self.time_out_animation

        self._driver.refresh()
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_step} Обновил страницу').infolog

        Logger(f'{config.indicator_test_step} Проверяю, что все значения сохранились').infolog

        for param_2 in self.choose_route['counter_params']:
            el = Find_element(driver = self._driver, path = self.choose_route['counter_params'][param_2]['check']['path'], wtime = 15).by_xpath_to_be_visibility_no_scroll
            text = el.text
            if text != self.choose_route['counter_params'][param_2]['check']['meaning']:
                name_screen = self.save_screen_shot
                allure.attach(self._driver.get_screenshot_as_png(), name='screen_shot', attachment_type=AttachmentType.PNG)
                Logger(f'{config.indicator_test_result_err} Маршрут для "{self.choose_route["counter_params"][param_2]["name"]}" не сохранился').errorlog
                Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
                assert text == self.choose_route['counter_params'][param_2]['check']['meaning']
            
        Logger(f'{config.indicator_test_result_suc} Выбранные маршруты сохранились').infolog
        Logger(f'{config.indicator_test_step} Возвращаю начальные значения').infolog

        el = Find_element(driver = self._driver, path = self.choose_route['edit'], wtime = 10).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        self.time_out_animation

        for param_3 in self.choose_route['counter_params']:
            el = Find_element(driver = self._driver, path = self.choose_route['counter_params'][param_3]['path']).by_xpath_to_be_clickable_no_scroll
            Actions(driver = self._driver).actions_click(el)
            self.time_out_animation

            el = Find_element(driver = self._driver, path = f"//*[@id='menu-']/div[3]/ul/li[text()='{self.choose_route['counter_params'][param_3]['check']['initial_values']}']", wtime = 10).by_xpath_to_be_visibility_no_scroll
            Actions(driver = self._driver).actions_click(el)
            self.time_out_animation

        el = Find_element(driver = self._driver, path = self.choose_route['save_route']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        self.time_out_animation



    

        




from argparse import Action
import random
import config
from src.base.base_page import Base_page
import allure
from allure_commons.types import AttachmentType

from src.base.constructor import Find_element   
from src.base.constructor import Placeholder    
from src.base.constructor import Actions        
from src.base.logger import Logger             


class Localuser(Base_page):

    __name = 'Класс для работы с элементами на странице "Локальные пользователи"'
    _report = "Страница 'Локальные пользователи'"
    __url = 'uta/admin/rolesTable'

    _els_when_create = {
        'path_to_el_but_create' : '//*[@id="tab-panel-tabpane-rolesTable"]/div/div[1]/div[3]/div/div/span/button',
        'path_to_el_but_save' : '//*[@id="tab-panel-tabpane-rolesTable"]/div/div[2]/div/div/div/table/tbody/tr[2]/td[1]/div/button[1]',
        'path_to_el_login' : '//*[@id="tab-panel-tabpane-rolesTable"]/div/div[2]/div/div/div/table/tbody/tr[2]/td[2]/div/div/input',
        'path_to_el_password' : '//*[@id="tab-panel-tabpane-rolesTable"]/div/div[2]/div/div/div/table/tbody/tr[2]/td[3]/div/div/input',
        'path_to_el_email' : '//*[@id="tab-panel-tabpane-rolesTable"]/div/div[2]/div/div/div/table/tbody/tr[2]/td[4]/div/div/input',
        'path_to_el_role' : '//*[@id="tab-panel-tabpane-rolesTable"]/div/div[2]/div/div/div/table/tbody/tr[2]/td[5]/div',
    }
    _role_administrator_nshr = '//*[@id="menu-"]/div[3]/ul/li[1]'
    _role_administrator = '//*[@id="menu-"]/div[3]/ul/li[2]'
    _role_control = '//*[@id="menu-"]/div[3]/ul/li[3]'
    _role_administrator_ib = '//*[@id="menu-"]/div[3]/ul/li[4]'
    _role_list = [_role_administrator_nshr, _role_administrator, _role_control, _role_administrator_ib]

    _but_edit_when_edit = '/td[1]/div/button[1]'
    _but_del_when_edit = '/td[1]/div/button[2]'
    _but_save_when_edit = '/td[1]/div/button[1]'
    _but_cancel_when_edit = '/td[1]/div/button[2]'

    _el_login_when_edit = '/td[2]/div/div/input'
    _el_password_when_edit = '/td[3]/div/div/input'
    _el_email_when_edit = '/td[4]/div/div/input'
    _el_role_when_edit = '/td[5]/div'


    param_create_new_user = []

    def generate_random_tests(self, count_test):
        for i in range(count_test):
            self.param_create_new_user.append(
                (
                    {'test_name' : 'Создание/Редактирование/Удаление локально пользователя'},
                    {'path' : self._els_when_create },
                    {'test_data' : { 
                    'login' : Base_page().generate_login,
                    'password' : Base_page().generate_password,
                    'email' : Base_page().generate_email,
                    'role' : random.choice(self._role_list),
                    'test_data_edit' : {
                        'login' : Base_page().generate_login,
                        'password' : Base_page().generate_password,
                        'email' : Base_page().generate_email,
                        'role' : random.choice(self._role_list),
                    },
                }
            },
                )
            )
        return len(self.param_create_new_user)


    def del_localuser(self, text, flag = None):
        self._driver.refresh()
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_step} Удаляю тестового пользователя ').infolog
        if type(text) != list:
            text = [text]
        counter = 1
        for user_text in text:
            self.time_out_animation
            counter += 1
            dinamic_path = Find_element(driver = self._driver).dynamic_path(text = user_text)
            if flag == False:
                if counter > len(text):
                    name_screen = self.save_screen_shot
                    allure.attach(self._driver.get_screenshot_as_png(), name='screen_shot', attachment_type=AttachmentType.PNG)
                    Logger(f'{config.indicator_test_result_err} Пользователя нет на странице').errorlog
                    Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
                    assert dinamic_path == 1
                try:   
                    el = Find_element(driver = self._driver, path = dinamic_path + self._but_del_when_edit ).by_xpath_to_be_clickable
                    Actions(driver = self._driver).click_js(el)
                    self.time_out_animation

                    el = Find_element(driver = self._driver, path = dinamic_path + self._but_save_when_edit ).by_xpath_to_be_clickable
                    Actions(driver = self._driver).click_js(el)
                    self.time_out_animation
                except Exception as e:
                    pass

            if dinamic_path == None and flag == False:
                Logger(f'{config.indicator_test_step} Пользователя нет на странице').infolog

            el = Find_element(driver = self._driver, path = dinamic_path + self._but_del_when_edit ).by_xpath_to_be_clickable
            Actions(driver = self._driver).click_js(el)
            self.time_out_animation

            el = Find_element(driver = self._driver, path = dinamic_path + self._but_save_when_edit ).by_xpath_to_be_clickable
            Actions(driver = self._driver).click_js(el)
            self.time_out_animation
            
            self._driver.refresh()
            self.time_out_after_refresh

            dinamic_path = Find_element(driver = self._driver).dynamic_path(text = user_text)
            if dinamic_path != None:
                name_screen = self.save_screen_shot
                allure.attach(self._driver.get_screenshot_as_png(), name='screen_shot', attachment_type=AttachmentType.PNG)
                Logger(f'{config.indicator_test_result_err} Пользователь не удалён').errorlog
                Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
                assert dinamic_path == None

            if flag == True:
                Logger(f'{config.indicator_test_result_suc} Пользователь удалён').infolog
            else:
                Logger(f'{config.indicator_test_result_suc} Пользователь удалён').infolog


    def edit_user(self, test_name, path, test_data):

        Logger(f'{config.indicator_test_step} Редактирую пользователя').infolog

        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = test_data['test_data']['login'])
        el = Find_element(driver = self._driver, path = dinamic_path + self._but_edit_when_edit, wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).click_js(el)
        Logger(f"{config.indicator_test_step} Нажал кнопку редактировать").infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._el_login_when_edit, wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).click_js(el)
        Placeholder(driver = self._driver).clear_place(el = el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['test_data_edit']['login'])
        Logger(f"{config.indicator_test_step} Отредактировал логин").infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._el_password_when_edit, wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).click_js(el)
        Placeholder(driver = self._driver).clear_place(el = el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['test_data_edit']['password'])
        Logger(f"{config.indicator_test_step} Отредактировал пароль").infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._el_email_when_edit, wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).click_js(el)
        Placeholder(driver = self._driver).clear_place(el = el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['test_data_edit']['email'])
        Logger(f"{config.indicator_test_step} Отредактировал почтовый адрес").infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._el_role_when_edit, wtime = 10).by_xpath_to_be_clickable
        Actions(self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = test_data['test_data']['test_data_edit']['role'], wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).click_js(el)
        Logger(f"{config.indicator_test_step} Изменил роль").infolog
        
        el = Find_element(driver = self._driver, path = dinamic_path + self._but_save_when_edit, wtime = 10).by_xpath_to_be_clickable
        Actions(driver = self._driver).click_js(el)
        Logger(f'{config.indicator_test_step} Нажал сохранить').infolog
        self.time_out_animation

        self._driver.refresh()
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_step} Обновил страницу').infolog

        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = test_data['test_data']['test_data_edit']['login'])
        if dinamic_path == None:
            name_screen = self.save_screen_shot
            allure.attach(self._driver.get_screenshot_as_png(), name='screen_shot', attachment_type=AttachmentType.PNG)
            Logger(f'{config.indicator_test_result_err} Не удалось найти пользователя').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            assert dinamic_path != None

        Logger(f'{config.indicator_test_step} Пользователь найден').infolog
        return test_data['test_data']['test_data_edit']['login']


    def create_new_user(self, test_name, path, test_data):
        try:
            self._driver.get(self._driver.url + self.__url)

            el = Find_element(driver = self._driver, path = path['path']['path_to_el_but_create'], wtime = 20).by_xpath_to_be_clickable_no_scroll
            Actions(driver = self._driver).actions_click(el)
            Logger(f'{config.indicator_test_step} Нажал кнопку добавить пользователя').infolog
            self.time_out_animation

            el = Find_element(driver = self._driver, path = path['path']['path_to_el_login'], wtime = 10).by_xpath_to_be_clickable_no_scroll
            Actions(driver = self._driver).actions_click(el)
            Placeholder(driver = self._driver).clear_place(el = el)
            Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['login'])
            Logger(f'{config.indicator_test_step} Ввёл логин').infolog

            el = Find_element(driver = self._driver, path = path['path']['path_to_el_password'], wtime = 10).by_xpath_to_be_clickable_no_scroll
            Actions(driver = self._driver).actions_click(el)
            Placeholder(driver = self._driver).clear_place(el = el)
            Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['password'])
            Logger(f'{config.indicator_test_step} Ввёл пароль').infolog

            el = Find_element(driver = self._driver, path = path['path']['path_to_el_email'], wtime = 10).by_xpath_to_be_clickable_no_scroll
            Actions(driver = self._driver).actions_click(el)
            Placeholder(driver = self._driver).clear_place(el = el)
            Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['email'])

            Logger(f'{config.indicator_test_step} Ввёл почтовый адрес').infolog

            el = Find_element(driver = self._driver, path = path['path']['path_to_el_role'], wtime = 10).by_xpath_to_be_clickable_no_scroll
            Actions(self._driver).actions_click_and_move(el)
            self.time_out_animation
            el = Find_element(driver = self._driver, path = test_data['test_data']['role'], wtime = 10).by_xpath_to_be_clickable_no_scroll
            Actions(driver = self._driver).actions_click(el)
            Logger(f'{config.indicator_test_step} Выбрал роль').infolog
            self.time_out_animation

            el = Find_element(driver = self._driver, path = path['path']['path_to_el_but_save'], wtime = 10).by_xpath_to_be_clickable_no_scroll
            Actions(driver = self._driver).actions_click(el)
            Logger(f'{config.indicator_test_step} Нажал сохранить').infolog
            self.time_out_animation

            self._driver.refresh()
            self.time_out_after_refresh
            Logger(f'{config.indicator_test_step} Обновил страницу').infolog

            Logger(f'{config.indicator_test_step} Ищу созданного пользователя').infolog

            dinamic_path = Find_element(driver = self._driver).dynamic_path(text = test_data['test_data']['login'])
            if dinamic_path == None:
                name_screen = self.save_screen_shot
                allure.attach(self._driver.get_screenshot_as_png(), name='screen_shot', attachment_type=AttachmentType.PNG)
                Logger(f'{config.indicator_test_result_err} Не удалось найти пользователя').errorlog
                Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
                assert dinamic_path != None

            Logger(f'{config.indicator_test_step} Пользователь найден').infolog

            return test_data['test_data']['login']

        except Exception as e:
            name_screen = self.save_screen_shot
            allure.attach(self._driver.get_screenshot_as_png(), name='screen_shot', attachment_type=AttachmentType.PNG)
            Logger(f'{config.indicator_test_result_err} Непредвиденная ошибка {e}').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            self.del_localuser(text = [test_data['test_data']['login'], test_data['test_data']['test_data_edit']['login']], flag = False)
            raise Exception(f"Непредвиденная ошибка {e}")


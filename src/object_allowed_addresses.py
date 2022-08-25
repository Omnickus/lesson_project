import config
from src.base.base_page import Base_page
import allure

# Импорт вспомогательных классов
from src.base.constructor import Find_element    # Поиск элементов
from src.base.constructor import Placeholder     # Взаимодействие с текстовыми полями, чек-боксами, радиокнопками и тд.
from src.base.constructor import Actions         # Разные действия
from src.base.logger import Logger               # Логгер
from src.base.logger import log_decorator        # Обёртка для логов


class Allowed_addresses(Base_page):

    __name = 'Класс для работы с элементами на странице "Разрешённые адреса"'
    _report = "Страница 'Разрешённые адреса'"
    __url = 'uta/admin/whiteList'

    _els_when_create = {
        'path_to_el_but_create' : '//*[@id="tab-panel-tabpane-whiteList"]/div/div[1]/div[3]/div/div/span/button',
        'path_to_el_but_save' : '//*[@id="tab-panel-tabpane-whiteList"]/div/div[2]/div/div/div/table/tbody/tr[2]/td[1]/div/button[1]',
        'path_to_el_login' : '//*[@id="tab-panel-tabpane-whiteList"]/div/div[2]/div/div/div/table/tbody/tr[2]/td[2]/div/div/input',
        'path_to_el_email' : '//*[@id="tab-panel-tabpane-whiteList"]/div/div[2]/div/div/div/table/tbody/tr[2]/td[3]/div/div/input',
    }

    _but_edit_when_edit = '/td[1]/div/button[1]'
    _but_del_when_edit = '/td[1]/div/button[2]'
    _but_save_when_edit = '/td[1]/div/button[1]'
    _but_cancel_when_edit = '/td[1]/div/button[2]'

    _el_login_when_edit = '/td[2]/div/div/input'
    _el_email_when_edit = '/td[3]/div/div/input'

    param_create_new_user = []

    def generate_random_tests(self, count_test):
        for i in range(count_test):
            self.param_create_new_user.append(
                (
                    {'test_name' : 'Создание/Редактирование/Удаление разрешённого адресата'},
                    {'path' : self._els_when_create },
                    {'test_data' : { 
                    'login' : Base_page().generate_login,
                    'email' : Base_page().generate_email,
                    'test_data_edit' : {
                        'login' : Base_page().generate_login,
                        'email' : Base_page().generate_email,
                    },
                }
            },
                )
            )
        return len(self.param_create_new_user)


    def del_allowed_address(self, text):
        self._driver.refresh()
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_step} Удаляю тестового пользователя ').infolog

        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = text)
        el = Find_element(driver = self._driver, path = dinamic_path + self._but_del_when_edit).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Нажал удалить').infolog

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
            Logger(f'{config.indicator_test_result_err} Не удалось удалить маршрут').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            assert dinamic_path == None

        Logger(f'{config.indicator_test_result_suc} Маршрут удалён').infolog


    def edit_user(self, *args, **kwargs):

        Logger(f'{config.indicator_test_step} Редактирую пользователя').infolog

        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = kwargs['test_data']['test_data']['login'])
        el = Find_element(driver = self._driver, path = dinamic_path + self._but_edit_when_edit, wtime = 10).by_xpath_to_be_clickable
        el.click()
        Logger(f"{config.indicator_test_step} Нажал кнопку редактировать").infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._el_login_when_edit, wtime = 10).by_xpath_to_be_clickable
        el.click()
        Placeholder(driver = self._driver).clear_place(el = el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = kwargs['test_data']['test_data']['test_data_edit']['login'])
        Logger(f"{config.indicator_test_step} Отредактировал логин").infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._el_email_when_edit, wtime = 10).by_xpath_to_be_clickable
        el.click()
        Placeholder(driver = self._driver).clear_place(el = el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = kwargs['test_data']['test_data']['test_data_edit']['email'])
        Logger(f"{config.indicator_test_step} Отредактировал почтовый адрес").infolog
        
        el = Find_element(driver = self._driver, path = dinamic_path + self._but_save_when_edit, wtime = 10).by_xpath_to_be_clickable
        el.click()
        Logger(f'{config.indicator_test_step} Нажал сохранить').infolog
        self.time_out_animation

        self._driver.refresh()
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_step} Обновил страницу').infolog

        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = kwargs['test_data']['test_data']['test_data_edit']['login'])
        if dinamic_path == None:
            name_screen = self.save_screen_shot
            Logger(f'{config.indicator_test_result_err} Не удалось найти пользователя').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            assert dinamic_path != None

        Logger(f'{config.indicator_test_step} Пользователь найден').infolog
        self.del_localuser(text = kwargs['test_data']['test_data']['test_data_edit']['login'])


    def create_new_user(self, test_name, path, test_data):
        try:
            self._driver.get(self._driver.url + self.__url)
            Logger(f'{config.indicator_test_page} {self._report}').infolog
            Logger(f'{config.indicator_test_name} {test_name["test_name"]}').infolog
            Logger(f'{config.indicator_test_param} Тестовые значения {test_data["test_data"]}').infolog

            el = Find_element(driver = self._driver, path = path['path']['path_to_el_but_create'], wtime = 20).by_xpath_to_be_clickable_no_scroll
            el.click()
            Logger(f'{config.indicator_test_step} Нажал кнопку добавить пользователя').infolog

            el = Find_element(driver = self._driver, path = path['path']['path_to_el_login'], wtime = 10).by_xpath_to_be_clickable_no_scroll
            el.click()
            Placeholder(driver = self._driver).clear_place(el = el)
            Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['login'])
            Logger(f'{config.indicator_test_step} Ввёл логин').infolog

            el = Find_element(driver = self._driver, path = path['path']['path_to_el_email'], wtime = 10).by_xpath_to_be_clickable_no_scroll
            el.click()
            Placeholder(driver = self._driver).clear_place(el = el)
            Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['email'])
            Logger(f'{config.indicator_test_step} Ввёл почтовый адрес').infolog

            el = Find_element(driver = self._driver, path = path['path']['path_to_el_but_save'], wtime = 10).by_xpath_to_be_clickable_no_scroll
            el.click()
            Logger(f'{config.indicator_test_step} Нажал сохранить').infolog
            self.time_out_animation

            self._driver.refresh()
            self.time_out_after_refresh
            Logger(f'{config.indicator_test_step} Обновил страницу').infolog

            Logger(f'{config.indicator_test_step} Ищу созданного пользователя').infolog

            dinamic_path = Find_element(driver = self._driver).dynamic_path(text = test_data['test_data']['login'])
            if dinamic_path == None:
                name_screen = self.save_screen_shot
                Logger(f'{config.indicator_test_result_err} Не удалось найти пользователя').errorlog
                Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
                assert dinamic_path != None

            Logger(f'{config.indicator_test_step} Пользователь найден').infolog

            return test_data['test_data']['login']

        except Exception as e:
            name_screen = self.save_screen_shot
            Logger(f'{config.indicator_test_result_err} Непредвиденная ошибка {e}').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            self.del_localuser(text = [test_data['test_data']['login'], test_data['test_data']['test_data_edit']['login']], flag = False)
            raise Exception(f"Непредвиденная ошибка {e}")


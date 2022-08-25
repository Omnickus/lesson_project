import config
from src.base.base_page import Base_page

# Импорт вспомогательных классов
from src.base.constructor import Find_element    # Поиск элементов
from src.base.constructor import Placeholder     # Взаимодействие с текстовыми полями, чек-боксами, радиокнопками и тд.
from src.base.constructor import Actions         # Разные действия
from src.base.logger import Logger               # Логгер
import allure

import random
import time

class Types_publications(Base_page):

    __name = 'Класс для работы с элементами на странице "Типы публикаций"'
    _report = "Страница 'Типы публикаций'"
    _url = 'uta/admin/publish'

    _but_edit_when_edit = '/td[2]/div/button[1]'
    _but_del_when_edit = '/td[2]/div/button[2]'
    _but_save_when_edit = '/td[2]/div/button[1]'
    _but_cancel_when_edit = '/td[2]/div/button[2]'

    _els_when_create = {
        'path_to_el_but_create' : '//*[@id="tab-panel-tabpane-publish"]/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div/span/button',
        'path_to_el_but_save' : '//*[@id="tab-panel-tabpane-publish"]/div/div[1]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[2]/div/button[1]',
        'path_to_el_name' : '//*[@id="tab-panel-tabpane-publish"]/div/div[1]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[3]/div/div/input',
        'path_to_el_type_publications' : '//*[@id="tab-panel-tabpane-publish"]/div/div[1]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[4]/div/div/input',
        'path_to_el_subtype_publications' : '//*[@id="tab-panel-tabpane-publish"]/div/div[1]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[5]/div/div/input',
        'path_to_el_file_type' : '//*[@id="tab-panel-tabpane-publish"]/div/div[1]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[6]/div/div/input',
        'path_to_el_email' : '//*[@id="tab-panel-tabpane-publish"]/div/div[1]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[7]/div/div/input',
        'path_to_el_regexp' : '//*[@id="tab-panel-tabpane-publish"]/div/div[1]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[8]/div/div/input',
    }
    _els_when_edit = {
        'path_to_el_name' : '/td[3]/div/div/input',
        'path_to_el_type_publications' : '/td[4]/div/div/input',
        'path_to_el_subtype_publications' : '/td[5]/div/div/input',
        'path_to_el_file_type' : '/td[6]/div/div/input',
        'path_to_el_email' : '/td[7]/div/div/input',
        'path_to_el_regexp' : '/td[8]/div/div/input',
    }

    type_publications = ['C', 'A', 'B']
    subtype_publications = ['bundle', 'docs', 'tk', 'releasetk', 'releasecoi', 'pm', 'npm']
    file_type = ['all_types', 'second123','random23123, rand_r13N']
    regexp = ['[A-Za-z0-9]', '[0-9.]+']

    params_create_publications = [
        (
            {
                'els_when_create' : _els_when_create
            },{
                'test_data' : {
                    'name' : Base_page().generate_login,
                    'type_publications' : random.choice(type_publications),
                    'subtype_publications' : random.choice(subtype_publications),
                    'file_type' : random.choice(file_type),
                    'email' : Base_page().generate_email,
                    'regexp' : random.choice(regexp),
                }
            }
        ),
    ]
    params_edit_publications = {
        
        'els_when_edit' : _els_when_edit,
        'test_data' : {
            'name' : Base_page().generate_login,
            'type_publications' : random.choice(type_publications),
            'subtype_publications' : random.choice(subtype_publications),
            'file_type' : random.choice(file_type),
            'email' : Base_page().generate_email,
            'regexp' : random.choice(regexp),
        }

    }


    def create_publications(self, path, test_data):

        el = Find_element(driver = self._driver, path = path['els_when_create']['path_to_el_but_create']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Logger(f'{config.indicator_test_step} Нажал создать').infolog

        el = Find_element(driver = self._driver, path = path['els_when_create']['path_to_el_name']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['name'])
        Logger(f'{config.indicator_test_step} Ввёл название').infolog

        el = Find_element(driver = self._driver, path = path['els_when_create']['path_to_el_type_publications']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['type_publications'])
        Logger(f'{config.indicator_test_step} Ввёл тип публикации').infolog

        el = Find_element(driver = self._driver, path = path['els_when_create']['path_to_el_subtype_publications']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['subtype_publications'])
        Logger(f'{config.indicator_test_step} Ввёл подтип публикации').infolog

        el = Find_element(driver = self._driver, path = path['els_when_create']['path_to_el_file_type']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['file_type'])
        Logger(f'{config.indicator_test_step} Ввёл типы файлов').infolog

        el = Find_element(driver = self._driver, path = path['els_when_create']['path_to_el_email']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['email'])
        Logger(f'{config.indicator_test_step} Ввёл почтовый адрес').infolog

        el = Find_element(driver = self._driver, path = path['els_when_create']['path_to_el_regexp']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['regexp'])
        Logger(f'{config.indicator_test_step} Ввёл регулярное выражение').infolog

        el = Find_element(driver = self._driver, path = path['els_when_create']['path_to_el_but_save']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Logger(f'{config.indicator_test_step} Нажал сохранить').infolog
        self.time_out_animation

        self._driver.refresh()
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_step} Обновил страницу').infolog

        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = test_data['test_data']['name'])
        if dinamic_path == None:
            name_screen = self.save_screen_shot
            Logger(f'{config.indicator_test_result_err} Не удалось найти созданный тип публикации').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            assert dinamic_path != None

        Logger(f'{config.indicator_test_result_suc} Созданный тип публикации найден').infolog

        # Возвращаю имя созданного типа публикации для использования в других тестах, например удалении или редактировании
        return test_data['test_data']['name']


    def delete_type_publications(self, name):
        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = name)

        el = Find_element(driver = self._driver, path = dinamic_path + self._but_del_when_edit).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        Logger(f'{config.indicator_test_step} Нажал удалить').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._but_save_when_edit).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        Logger(f'{config.indicator_test_step} Нажал подтвердить удаление').infolog

        self._driver.refresh()
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_step} Обновил страницу').infolog

        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = name)
        if dinamic_path != None:
            name_screen = self.save_screen_shot
            Logger(f'{config.indicator_test_result_err} Не удалось удалить тип публикации').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            assert dinamic_path == None

        Logger(f'{config.indicator_test_result_suc} Тип публикации удалён').infolog


    def edit_type_publications(self, name):
        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = name)
        
        el = Find_element(driver = self._driver, path = dinamic_path + self._but_edit_when_edit).by_xpath_to_be_clickable
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        Logger(f'{config.indicator_test_step} Нажал редактировать').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self.params_edit_publications['els_when_edit']['path_to_el_name']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Placeholder(driver = self._driver).clear_place(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = self.params_edit_publications['test_data']['name'])
        Logger(f'{config.indicator_test_step} Ввёл название').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self.params_edit_publications['els_when_edit']['path_to_el_type_publications']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Placeholder(driver = self._driver).clear_place(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = self.params_edit_publications['test_data']['type_publications'])
        Logger(f'{config.indicator_test_step} Ввёл тип публикации').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self.params_edit_publications['els_when_edit']['path_to_el_subtype_publications']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Placeholder(driver = self._driver).clear_place(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = self.params_edit_publications['test_data']['subtype_publications'])
        Logger(f'{config.indicator_test_step} Ввёл подтип публикации').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self.params_edit_publications['els_when_edit']['path_to_el_file_type']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Placeholder(driver = self._driver).clear_place(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = self.params_edit_publications['test_data']['file_type'])
        Logger(f'{config.indicator_test_step} Ввёл типы файлов').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self.params_edit_publications['els_when_edit']['path_to_el_email']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Placeholder(driver = self._driver).clear_place(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = self.params_edit_publications['test_data']['email'])
        Logger(f'{config.indicator_test_step} Ввёл почтовый адрес').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self.params_edit_publications['els_when_edit']['path_to_el_regexp']).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Placeholder(driver = self._driver).clear_place(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = self.params_edit_publications['test_data']['regexp'])
        Logger(f'{config.indicator_test_step} Ввёл регулярное выражение').infolog

        el = Find_element(driver = self._driver, path = dinamic_path + self._but_save_when_edit).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click(el)
        Logger(f'{config.indicator_test_step} Нажал сохранить').infolog
        self.time_out_animation

        self._driver.refresh()
        self.time_out_after_refresh
        Logger(f'{config.indicator_test_step} Обновил страницу').infolog

        dinamic_path = Find_element(driver = self._driver).dynamic_path(text = self.params_edit_publications['test_data']['name'])
        if dinamic_path == None:
            name_screen = self.save_screen_shot
            Logger(f'{config.indicator_test_result_err} Тип публикации не отредактировался').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            self.delete_type_publications(name = name)
            assert dinamic_path != None

        Logger(f'{config.indicator_test_result_suc} Тип публикации отредактирован').infolog

        return self.params_edit_publications['test_data']['name']
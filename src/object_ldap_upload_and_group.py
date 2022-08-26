import config
from src.base.base_page import Base_page
from selenium.common.exceptions import TimeoutException
import allure

from src.base.constructor import Find_element  
from src.base.constructor import Placeholder  
from src.base.constructor import Actions      
from src.base.logger import Logger    
from src.base.logger import log_decorator  



import time

class Ldap_upload_and_group(Base_page):

    __name = 'Класс для работы с элементами на странице "Выгрузка групп LDAP"'
    _report = "Страница 'Выгрузка групп LDAP'"
    __url = 'uta/admin/ldap'
    __url_group = 'uta/admin/groups'
    __test_name = 'Выгрузка группы LDAP/Редактирование/Удаление'

    name_group_for_upload = [('mpp-controlers')]
    __but_upload_group = '//*[@id="tab-panel-tabpane-ldap"]/div/div/div/div/div/button'
    __el_confirm_upload = '//*[@id="simple-popover"]/div[3]/p'

    __but_del_when_edit = '/td[1]/div/button[2]'
    __but_save_when_edit = '/td[1]/div/button[1]'

    @allure.step
    @log_decorator
    def upload_group_ldap(self, group):
        self._driver.get(self._driver.url + self.__url)
        Logger(f'{config.indicator_test_page} {self._report}').infolog
        Logger(f'{config.indicator_test_name} {self.__test_name}').infolog
        Logger(f'{config.indicator_test_param} Тестовые значения {group}').infolog

        Logger(f'{config.indicator_test_step} Ищу группу на странице').infolog
        el = Find_element(driver = self._driver, path = f'//*[@id="tab-panel-tabpane-ldap"]/div/div/ul//*[contains(text(),"{group}")]', wtime = 15).by_xpath_to_be_visibility
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Выбрал группу').infolog

        el = Find_element(driver = self._driver, path = self.__but_upload_group, wtime = 15).by_xpath_to_be_clickable
        el.click()
        Logger(f'{config.indicator_test_step} Нажал выгрузть группу').infolog

        el = Find_element(driver = self._driver, path = self.__el_confirm_upload, wtime = 15).by_xpath_to_be_visibility
        el.click()

        Logger(f'{config.indicator_test_result_suc} Группа выгружена').infolog

        pass
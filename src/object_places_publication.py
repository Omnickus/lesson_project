import config
from src.base.base_page import Base_page

from src.base.constructor import Find_element    
from src.base.constructor import Placeholder     
from src.base.constructor import Actions         
from src.base.logger import Logger              


class Places_publication(Base_page):

    __name = 'Ксласс с элементами страницы Места публикации'
    _report = "Страница 'места публикации'"
    _url = 'uta/admin/publish#places'

    path_for_create = {
        'el_but_create' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/span/button',
        'el_but_save' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[1]/div/button[1]',
        'el_name' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[2]/div/div/input',
        'el_description' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[3]/div/div/input',
        'el_type_publication' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[4]/div/div/div',
        'el_name_catalog_how_name_mail' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[5]/span/span[1]/input',
        'el_user_name' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[6]/div/div/input',
        'el_user_password' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[7]/div/div/input',
        'el_grant_rights' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[8]/span/span[1]/input',
        'el_api_key' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[9]/div/div/input',
        'el_protocol' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[11]/div/div/div',
        'el_server' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[12]/div/div/input',
        'el_port' : '//*[@id="tab-panel-tabpane-publish"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[13]/div/div/input',
    }

    choose_protocol = {
        'http' : '//*[@id="menu-"]/div[3]/ul/li[1]',
        'https' : '//*[@id="menu-"]/div[3]/ul/li[2]',
        'ftp' : '//*[@id="menu-"]/div[3]/ul/li[3]',
        'sftp' : '//*[@id="menu-"]/div[3]/ul/li[4]',
        'smb' : '//*[@id="menu-"]/div[3]/ul/li[5]',
    }
    choose_type_publication = {
        'catalog' : '//*[@id="menu-"]/div[3]/ul/li[1]',
        'ftp_server' : '//*[@id="menu-"]/div[3]/ul/li[2]',
        'redirect_mail' : '//*[@id="menu-"]/div[3]/ul/li[3]',
        'smb_server' : '//*[@id="menu-"]/div[3]/ul/li[4]',
        'gitlab' : '//*[@id="menu-"]/div[3]/ul/li[5]',
        'artifactory' : '//*[@id="menu-"]/div[3]/ul/li[6]',
    }

    params_create_palace_publication = [
        (
            {'test_data' : {
                'test_name' : 'Seleniun_place_publication_' + str(Base_page().random_int(1000, 99999)),
                'test_description' : 'Seleniun_description_' + str(Base_page().random_int(1000, 99999)),
                'test_type_publication' : choose_type_publication,
                'test_name_catalog_how_name_mail' : True,
                'test_user_name' : 'Selen_user_' + str(Base_page().random_int(1000, 99999)),
                'test_user_password' : Base_page().generate_password,
                'test_grant_rights' : True,
                'test_api_key' : 'kawd^*akjwdi7a^&)(((%$%wd123',
                'test_protocol' : choose_protocol['https'] ,
                'test_server' : '172.29.39.144',
                'test_port' : '8888'
            }}
        )
    ]
    


    def create_new_place_publication(self, test_data):

        el = Find_element(driver = self._driver, path = self.path_for_create['el_but_create'], wtime = 20).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f'{config.indicator_test_step} Нажал создать новое место публикации').infolog

        el = Find_element(driver = self._driver, path = self.path_for_create['el_name'], wtime = 20).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['test_name'])
        Logger(f'{config.indicator_test_step} Ввёл название').infolog

        el = Find_element(driver = self._driver, path = self.path_for_create['el_description'], wtime = 20).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        Placeholder(driver = self._driver).char_by_char(el = el, text = test_data['test_data']['test_description'])
        Logger(f'{config.indicator_test_step} Ввёл описание').infolog

        el = Find_element(driver = self._driver, path = self.path_for_create['el_type_publication'], wtime = 20).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        el = Find_element(driver = self._driver, path = test_data['test_data']['test_type_publication']['catalog'], wtime = 20).by_xpath_to_be_clickable_no_scroll
        Actions(driver = self._driver).actions_click_and_move(el)
        self.time_out_animation
        Logger(f"{config.indicator_test_step} Выбрал тип публикации").infolog
        return True
        el = Find_element(driver = self._driver, path = self.path_for_create['el_name_catalog_how_name_mail'], wtime = 20).by_xpath_to_be_visibility_no_scroll
        if test_data['test_data']['test_name_catalog_how_name_mail'] == True:
            Actions(driver = self._driver).actions_click_and_move(el)
        Logger(f"{config.indicator_test_step} Установил check-box для имени каталога").infolog


        import time
        time.sleep(20)




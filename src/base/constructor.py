from src.base.logger import Logger

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Работа с клаватурой
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import itertools
import re

# Настройки конфигурации
import config


# Другие импорты
import time



class Find_element:
    """
    Класс для поиска элементов.
    """
    __name = 'Поиск элементов'

    def __new__(cls, *args, **kwargs):
        """
        Разрешается создать объект класса в том случае, 
        если будет передана ссылка на объект драйвера.
        """
        __count_erorr = 0
        if len(args) > 0:
            __count_erorr += 1
        try:
            if len(kwargs) < 1:
                __count_erorr += 1
            if type(kwargs['driver']):
                pass 
            else:
                __count_erorr += 1
            try:
                if type(kwargs['path']) != str:
                    __count_erorr += 1
                if type(kwargs['wtime']) != int:
                    __count_erorr += 1
            except:
                pass
            if __count_erorr == 0:
                return super().__new__(cls)
            else:
                Logger(f"Невозможно создать объект класса Find_element, т.к количество ошибок при создании превышает допустимое значени.").debuglog
                return None

        except Exception as e:
            Exception(f"Не возможно создать объект класса Find_element. Ошибка - {e}")
            Logger(f"Не возможно создать объект класса Find_element. Ошибка - {e}.").debuglog
            return None

    def __init__(self, path = None, wtime = None, driver = None):
        self._path = path               # Путь до елемента (xpath, id, selector и тд.)
        self._wtime = wtime             # Время ожидания элемента на странице (Если None будет использоваться время из config, переменная default_timeout)
        self._driver = driver           # Ссылка на объект драйвера
        if wtime == None:
            self._wtime = int(config.default_timeout)
    
    @property
    def by_xpath_to_be_clickable_no_scroll(self):
        el = WebDriverWait( self._driver, self._wtime ).until(EC.element_to_be_clickable(( By.XPATH, self._path )))
        return el

    @property
    def by_xpath_to_be_clickable(self):
        el = WebDriverWait( self._driver, self._wtime ).until(EC.element_to_be_clickable(( By.XPATH, self._path )))
        self._driver.execute_script("arguments[0].scrollIntoView(true);", el)
        return el

    @property
    def by_xpath_to_be_visibility(self):
        el = WebDriverWait( self._driver, self._wtime ).until(EC.visibility_of_element_located(( By.XPATH, self._path )))
        self._driver.execute_script("arguments[0].scrollIntoView(true);", el)
        return el
    
    @property
    def by_xpath_to_be_visibility_no_scroll(self):
        el = WebDriverWait( self._driver, self._wtime ).until(EC.visibility_of_element_located(( By.XPATH, self._path )))
        return el

    @property
    def by_xpath_get_elements(self):
        el = WebDriverWait( self._driver, self._wtime ).until(EC.visibility_of_all_elements_located(( By.XPATH, self._path )))
        return el

    def xpath_soup(self, el):
        """
        Generate xpath of soup element
        :param element: bs4 text or node
        :return: xpath as string
        """
        components = []
        child = el if el.name else el.parent
        for parent in child.parents:
            """
            @type parent: bs4.element.Tag
            """
            previous = itertools.islice(parent.children, 0,parent.contents.index(child))
            xpath_tag = child.name
            xpath_index = sum(1 for i in previous if i.name == xpath_tag) + 1
            components.append(xpath_tag if xpath_index == 1 else '%s[%d]' % (xpath_tag, xpath_index))
            child = parent
        components.reverse()
        return '/%s' % '/'.join(components)
    
    def dynamic_path(self, text):
        i = 0
        while i < config.jump_count:
            Logger(f'dynamic_path - ищу с использованием текста {text}').debuglog
            html = self._driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            el = soup.find(string=re.compile(text))
            if el != None:
                Logger(f'dynamic_path - найденный элемент {el}').debuglog
                s = self.xpath_soup(el = el)
                s = s[::-1]
                count = 0
                for i in s: 
                    if i == '/' or i == '\\': 
                        count += 1 
                        break 
                    count += 1
                s = s[::-1]
                s = s[0:len(s) - (count)]
                Logger(f'dynamic_path - Абсолютный путь построен {s}').debuglog
                return s
            i += 1
            time.sleep(config.time_out_new_jump)
        if i == config.jump_count:
            return None
        




class Placeholder:
    """
    Класс для работы с текстовыми полями, чек-боксами, радиокнопками.
    """
    __name = 'Работа с плэйсхордерами, радио кнопками, чек-боксами'

    def __new__(cls, *args, **kwargs):
        """
        Разрешается создать объект класса в том случае, 
        если будет передана ссылка на объект драйвера.
        """
        __count_erorr = 0
        if len(args) > 0:
            __count_erorr += 1
        try:
            if type(kwargs['driver']) != int and type(kwargs['driver']) != str:
                pass 
            else:
                __count_erorr += 1
            
            if __count_erorr == 0:
                return super().__new__(cls)
            else:
                Logger(f"Невозможно создать объект класса Placeholder, т.к количество ошибок при создании превышает допустимое значени.").debuglog
                return None

        except Exception as e:
            Exception(f"Не возможно создать объект класса Placeholder. Ошибка - {e}")
            Logger(f"Не возможно создать объект класса Placeholder. Ошибка - {e}.").debuglog
            return None

    def __init__(self, driver):
        self._driver = driver
    
    def clear_place(self, el):
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(Keys.BACKSPACE)

    def char_by_char(self, el, text):
        for i in text:
            el.send_keys(i)
            time.sleep(0.01)


    
class Actions:
    """
    Класс для работы с действиями браузера
    """
    __name = 'Класс для работы с действиями браузера (Actions)'

    def __init__(self, driver):
        self._driver = driver
        self._actions = ActionChains(self._driver)

    def perform_actions(self):
        """ Выполнение и очистка очереди действий """
        self._actions.perform()
        self._actions.reset_actions()
        try:
            for device in self._actions.w3c_actions.devices:
                device.clear_actions()
        except Exception as e:
            pass

    def click_js(self, el):
        self._driver.execute_script("arguments[0].click();", el)

    def actions_click_and_move(self, el):
        self._actions.move_to_element(el)
        time.sleep(0.2)
        self._actions.click(el)
        self.perform_actions()

    def actions_click(self, el):
        self._actions.click(el)
        self.perform_actions()


    def change_browser_zoom(self, side = None, counter = None):
        if side == None:
            side = '-'
        if counter == None:
            counter = 1
        if side in ('-', '+'):
            for i in range(0, counter):
                self._actions.key_down(Keys.CONTROL)
                self._actions.send_keys(side)
        pass

    

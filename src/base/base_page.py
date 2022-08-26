from random import random
import config
import time
import pathlib
import os
import random


class Base_page:

    __logins = [
        "Yline", "Snowterror", 'Dianalanim', 'Bloodstone', 'Thetanadar', 'Moogukinos', 'Bladeflame', 'Brightbrew', 'Kathridred', 'JoJoshakar', 'Fenritilar', 'sicuvoup3tif', 
        'Delahuginn', 'Cordanadar', 'Blackgrove', 'Centrithis', 'Thetalanim', '64dy0ep7romi', 'Goldterror', 'Shadowwood', 'Shadowbrew', 'Halsier', 'Flamestaff', 'Ishnntrius', 
        'xo2wba5ve17u', 'Dianawield', 'Dalagamand', 'Felhanadar', 'Spellblade', 'Renayah', 'Steelshade', 'yr0ne543wha2', 'Dawnmaster', 'Oghmajurus', 'Lightbrand', 'Maushicage', 
        'wla52udge9da', 'Norahmandres', 'Umikaiyat', 'Magecaster', 'Dawnwarden', 'Fenriramar', 'Tygoshakar', 'Felhagrinn', 'Fordrerana', 'Starshaper', 'Stoneshade', 'Runebinder', 
        'Akinolabar', 'hiec3udrayts'
    ]
    __email = [
        'yopmail.com', 'gmail.com', 'roberts.net', 'fahey.info', 'yahoo.com', 'cormier.com', 'hotmail.com', 'mail.com', 'lind.org', 'casper.com', 'schoen.com',
        'rocketmail.com', 'yahoomail.com', 'googlemail.com', 'aol.com', 'yandex.ru', 'rambler.ru', 'cbr.ru', 'live.com'
    ]
    __password = [
        '6?{9}TO*kK', 'cwRZjS1kNa', 'xOF09zMro5', 'K%fI|w8kU9', '7~|vn3c77T', 'I2$4@~bKbk', 'jF5Wd@V|$Q', 'Ey*edEi@uf', 'BGr4JVLm*k', 'YER2b3C', 'NIuR1Qq', 'rzGLMvX', '3V1YB0V'
    ]
    
    def __init__(self, driver = None) -> None:
        self._driver = driver

    @property
    def save_screen_shot(self):
        """ Общий метод создания скриншотов. Наследуейте класс Base_page и воспользуйтесь self.save_screen_shot """
        name = str(time.monotonic()).replace('.', '') + '_.' + config.image_extension
        self._driver.save_screenshot( name )
        e = os.popen(f'cp {str(pathlib.Path().absolute()) + "/" + name} {str(pathlib.Path().absolute()) + "/" + config.path_screen_shot + "/" + name}')
        s = os.popen( f'rm {str(pathlib.Path().absolute()) + "/" + name}' )
        return name

    @property
    def time_out_animation(self):
        """ Используейте в тестах, если вам нужно некоторое ожидание, когда проёдёт анимация. """
        time.sleep(config.default_timeout_animation)

    @property
    def time_out_after_refresh(self):
        """ Используейте в тестах, если вам нужно некоторое ожидание, после перезагрузки сраницы. """
        time.sleep(config.default_timeout_animation)

    @property
    def time_out_free(self):
        """ Используейте в тестах, если вам нужно некоторое ожидание. Ни от чего не зависящий параметр """
        time.sleep(config.time_out_free)
    
    @property
    def generate_login(self):
        return 'Selen' + '_' + random.choice(self.__logins) + str(random.randint(1000, 999999))
    
    @property
    def generate_email(self):
        return random.choice(self.__logins) + str(random.randint(1000, 999999)) + '@' + random.choice(self.__email)

    @property
    def generate_password(self):
        return random.choice(self.__password) + str(random.randint(0, 99999))

    def random_int(self, _from, _before):
        return int(random.randint(_from, _before))


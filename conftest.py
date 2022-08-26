import pytest
import config
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.service import Service as SafariService

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from elements import Url_page

import os
import pathlib
import time


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default=Url_page.authorization_page)
    parser.addoption("--driver", action="store", default="/opt/drivers/")
    parser.addoption("--executor", action="store", default='127.0.0.1')
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--bv")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--driver")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    if executor == None:
        if browser == "chrome":
            service = ChromiumService(executable_path=drivers + "chromedriver")
            try:
                driver = webdriver.Chrome(service=service)
            except Exception as e:
                options = webdriver.ChromeOptions()
                driver_path = drivers + "chromedriver"
                driver = webdriver.Chrome(  
                                        executable_path = driver_path,
                                        options = options
                                    )
        elif browser == "firefox":
            service = FFService(executable_path=drivers + "geckodriver")
            try:
                driver = webdriver.Firefox(service=service)
            except Exception as e:
                options = webdriver.FirefoxOptions()
                driver_path = drivers + "geckodriver"
                driver = webdriver.Chrome(  
                                        executable_path = driver_path,
                                        options = options
                                    )
        elif browser == "Edge":
            service = EdgeService(executable_path=drivers + "edge")
            try:
                driver = webdriver.Edge(service=service)
            except Exception as e:
                options = webdriver.FirefoxOptions()
                driver_path = driver + "edge"
                driver = webdriver.Chrome(  
                                        executable_path = driver_path,
                                        options = options
                                    )
        else:
            driver = SafariService()
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        capabilities = {
            "browserName": browser,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs,
                "acceptInsecureCerts": True,
            }
        }   
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=capabilities,
        )


    def fin():
        driver.quit()
    request.addfinalizer(fin)

    driver.maximize_window()

    driver.get(url)
    driver.url = url

    el = driver.find_element_by_xpath('//*[@id="details-button"]')
    el.click()
    el = driver.find_element_by_xpath('//a[@id="proceed-link"]')
    el.click()


    el = driver.find_element_by_xpath('//input[@placeholder="Логин"]')
    el.click()
    el.send_keys('admin')
    el = driver.find_element_by_xpath('//input[@placeholder="Пароль"]')
    el.click()
    el.send_keys('admin')
    el = driver.find_element_by_xpath('//button[@type="submit"]')
    el.click()
    el = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(( By.XPATH, '//*[@id="root"]/nav[1]/a[1]/img' )))
    if not el:
        raise Exception('Не удалось вторизоваться в приложении')

    return driver


def pytest_sessionstart(session):
    """ Функция вызывается перед прогоном тестов """

    print(f"\n***** Уровень логирования : {config.log_level} *****")
    time.sleep(0.5)
    print(f"\n***** Удаляю прошлые скриншоты *****")
    time.sleep(0.5)
    images_list = os.listdir(str(pathlib.Path().absolute()) + "/" + config.path_screen_shot + "/")
    for image in images_list:
        try:
            os.popen( f'rm {str(pathlib.Path().absolute()) + "/" + config.path_screen_shot + "/" + image}' )
        except Exception as e:
            print(f"Ошибка при удалении скриншота - {e}")
    print(f"\n***** Удаляю прошлые логи *****")
    time.sleep(0.5)
    try:
        path = str(pathlib.Path().absolute()) + '/src/base/logs/'
        logs_list = os.listdir( path )
        for i in logs_list:
            os.popen( f'rm {str(pathlib.Path().absolute())}/src/base/logs/{i}' )
    except Exception as e:
        print(f"Ошибка при удалении прошлых логов - {e}")
    print(f"\n***** Удаляю прошлый отчёт *****")
    time.sleep(0.5)
    try:
        os.popen( f'rm {str(pathlib.Path().absolute()) + "/" + config.name_file_for_docx_report_from_log}' )
    except Exception as e:
        print(f"Ошибка при удалении прошлого отчёта - {e}")
    time.sleep(0.5)
    from src.object_localuser import Localuser
    print(f"\n***** Генерирую тесты для {Localuser._report}: Количество сгенерированных тестов {Localuser().generate_random_tests(count_test = 1)} *****")
    time.sleep(0.5)
    from src.object_allowed_addresses import Allowed_addresses
    print(f"\n***** Генерирую тесты для {Allowed_addresses._report}: Количество сгенерированных тестов {Allowed_addresses().generate_random_tests(count_test = 5)} *****")
    time.sleep(0.5)
    print(f"\n***** Запускаю тесты со следующими параметрами *****")
    print(f"----- Флаг создания отчёта - {config.flag_create_report}")


def pytest_sessionfinish(session, exitstatus):
    """ Функция вызывается после завершения всего прогона """
    print(f"\n***** Завершаю тестирование *****")
    from src.base.docx_reports import Report_docx
    flag_report = config.flag_create_report
    if flag_report == False:
        return None
    print(f"\n***** Готовлю отчёт DOCX *****")
    path_report = str(pathlib.Path().absolute()) + config.name_file_for_docx_report_from_log
    if os.path.exists(path_report) != True:
        Report_docx().create_docx()




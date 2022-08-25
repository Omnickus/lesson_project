import config
from src.base.base_page import Base_page
import time
import allure
from allure_commons.types import AttachmentType

# Импорт вспомогательных классов
from src.base.constructor import Find_element    # Поиск элементов
from src.base.constructor import Placeholder     # Взаимодействие с текстовыми полями, чек-боксами, радиокнопками и тд.
from src.base.constructor import Actions         # Разные действия
from src.base.logger import Logger               # Логгер
from src.base.logger import log_decorator

class System(Base_page):

    __name = 'Ксласс с элементами системы'
    __report = "Страница 'Cистема'"

    param = [
                (   {'test_name' : 'Web-адрес Zabbix'},
                    {'path_to_el' : '//*[@id="settings_setup_field_zabbix_url"]'},
                    {
                        'correct_test' :    [{ 'text' : 'http://172.29.39.69/login', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'пользователь для подключения к серверу ldap'},
                    {'path_to_el' : '//*[@id="settings_setup_field_ldap_user"]'},
                    {
                        'correct_test' :    [{ 'text' : config.default_user, 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                # (   {'test_name' : 'пароль для подключения к серверу ldap'},
                #     {'path_to_el' : '//*[@id="settings_setup_field_ldap_password"]'},
                #     {
                #         'correct_test' :    [{ 'text' : config.default_passwd, 'status' : True }],
                #         'string' :          [{ 'text' : config.default_string, 'status': True }],
                #         'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                #         'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                #         'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                #     }
                # ),
                (   {'test_name' : 'Сервер ldap'},
                    {'path_to_el' : '//*[@id="settings_setup_field_ldap_host"]'},
                    {
                        'correct_test' :    [{ 'text' : 'https://111.111.111.111', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'порт для подключения к серверу ldap'},
                    {'path_to_el' : '//*[@id="settings_setup_field_ldap_port"]'},
                    {
                        'correct_test' :    [{ 'text' : '444', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : '12345', 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Фильтр LDAP'},
                    {'path_to_el' : '//*[@id="settings_setup_field_ldap_filter"]'},
                    {
                        'correct_test' :    [{ 'text' : 'OU=test,DC=test,DC=test', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'корневая директория в ldap'},
                    {'path_to_el' : '//*[@id="settings_setup_field_ldap_base_dn"]'},
                    {
                        'correct_test' :    [{ 'text' : 'dc=test,dc=test,dc=test', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'Добавление групп пользователей в Хранилище Исходного Кода'},
                    {'path_to_el' : '//*[@id="settings_setup_field_gitlab_add_members_group"]'},
                    {
                        'correct_test' :    [{ 'text' : 'true', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Добавление групп пользователей maintainers в Хранилище Исходного Кода'},
                    {'path_to_el' : '//*[@id="settings_setup_field_gitlab_add_members_group_maintaners"]'},
                    {
                        'correct_test' :    [{ 'text' : 'test_user', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'Добавление пользователей в Хранилище Исходного Кода'},
                    {'path_to_el' : '//*[@id="settings_setup_field_gitlab_add_members"]'},
                    {
                        'correct_test' :    [{ 'text' : 'true', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'API сервис Camunda'},
                    {'path_to_el' : '//*[@id="settings_setup_field_cammunda_service_ip"]'},
                    {
                        'correct_test' :    [{ 'text' : 'https://111.111.11.11:9090', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Добавление пользователей maintainers в Хранилище Исходного Кода'},
                    {'path_to_el' : '//*[@id="settings_setup_field_gitlab_add_members_maintaners"]'},
                    {
                        'correct_test' :    [{ 'text' : 'test_user', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'Добавление групп пользователей reporters в Хранилище Исходного Кода'},
                    {'path_to_el' : '//*[@id="172.29.39.37Не определен"]//*[@id="settings_setup_field_gitlab_add_members_group_reporters"]'},
                    {
                        'correct_test' :    [{ 'text' : 'test_user', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'Добавление пользователей reporters в Хранилище Исходного Кода'},
                    {'path_to_el' : '//*[@id="settings_setup_field_gitlab_add_members_reporters"]'},
                    {
                        'correct_test' :    [{ 'text' : 'test_user', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'Уровень логирования модуля Публикация данных'},
                    {'path_to_el' : '//*[@id="172.29.39.37Не определен"]//*id="settings_setup_field_publisher_logger_level"]'},
                    {
                        'correct_test' :    [{ 'text' : 'DEBUG', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Путь к curl'},
                    {'path_to_el' : '//*[@id="settings_setup_field_curl_path"]'},
                    {
                        'correct_test' :    [{ 'text' : 'test_curl', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'Размер части архива для поставок, пересылаемых на почту'},
                    {'path_to_el' : '//*[@id="settings_setup_field_zip_split_length"]'},
                    {
                        'correct_test' :    [{ 'text' : '9999999', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : '123456789', 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Максимальное время ожидания выполнения REST запроса'},
                    {'path_to_el' : '//*[@id="settings_setup_field_read_api_timeout"]'},
                    {
                        'correct_test' :    [{ 'text' : '9999999', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : '123456789', 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Проверка правил'},
                    {'path_to_el' : '//*[@id="settings_setup_field_gitlab_rules"]'},
                    {
                        'correct_test' :    [{ 'text' : 'true', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Очередь публикации репозиториев в Gitlab'},
                    {'path_to_el' : '//*[@id="settings_setup_field_gitlab_queue_publish"]'},
                    {
                        'correct_test' :    [{ 'text' : '["sharedlib","orm","dossier","...","main"]', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Путь к git'},
                    {'path_to_el' : '//*[@id="settings_setup_field_git_path"]'},
                    {
                        'correct_test' :    [{ 'text' : 'test_git', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'Список файлов для сравнения'},
                    {'path_to_el' : '//*[@id="settings_setup_field_gitlab_diff_file_list"]'},
                    {
                        'correct_test' :    [{ 'text' : '["config/%repo%/params.py","params.py"]', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'Список репозиториев на diff'},
                    {'path_to_el' : '[//*[@id="172.29.39.37Не определен"]//*@id="settings_setup_field_gitlab_diff_repo_list"]'},
                    {
                        'correct_test' :    [{ 'text' : '["cos-config","test","test"]', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Проверка changelog'},
                    {'path_to_el' : '//*[@id="settings_setup_field_gitlab_changelog_verify"]'},
                    {
                        'correct_test' :    [{ 'text' : 'true', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Проверка diff'},
                    {'path_to_el' : '//*[@id="settings_setup_field_gitlab_diff_verify"]'},
                    {
                        'correct_test' :    [{ 'text' : 'true', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Репозитории для проверки changelog.<name_system>'},
                    {'path_to_el' : '//*[@id="settings_setup_field_gitlab_changelog_repo_list"]'},
                    {
                        'correct_test' :    [{ 'text' : '["cos","fps","ckps","hdm","sdm","ars","aspd"]', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Файлы для проверки changelog.<name_system>'},
                    {'path_to_el' : '//*[@id="settings_setup_field_gitlab_changelog_file_list"]'},
                    {
                        'correct_test' :    [{ 'text' : '["changelog.main","changelog.testpbo"]', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Каталог с PID сервисами'},
                    {'path_to_el' : '//*[@id="settings_setup_field_service_pid_folder"]'},
                    {
                        'correct_test' :    [{ 'text' : '/test/test/test_catalog', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Проверка МПП на других площадках'},
                    {'path_to_el' : '//*[@id="settings_setup_field_system_fault_tolerance"]'},
                    {
                        'correct_test' :    [{ 'text' : 'false', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                # (   {'test_name' : 'Пароль пользователя на почтовом сервере'},
                #     {'path_to_el' : '//*[@id="settings_setup_field_mail_pass"]'},
                #     {
                #         'correct_test' :    [{ 'text' : 'false', 'status' : True }],
                #         'string' :          [{ 'text' : config.default_string, 'status': True }],
                #         'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                #         'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                #         'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                #     }
                # ),
                (   {'test_name' : 'Входящий каталог обработки'},
                    {'path_to_el' : '//*[@id="settings_setup_field_module_income_folder"]'},
                    {
                        'correct_test' :    [{ 'text' : '/test1/test2/test3/test4', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Сервер SMTP'},
                    {'path_to_el' : '//*[@id="settings_setup_field_mail_smtp_host"]'},
                    {
                        'correct_test' :    [{ 'text' : 'test.test.test.ru', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'Порт SMTP'},
                    {'path_to_el' : '//*[@id="settings_setup_field_mail_smtp_port"]'},
                    {
                        'correct_test' :    [{ 'text' : '587', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : '12345', 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Каталог сохранения временных почтовых файлов'},
                    {'path_to_el' : '//*[@id="172.29.39.37Не определен"]//*[@id="settings_setup_field_mail_attach_folder"]'},
                    {
                        'correct_test' :    [{ 'text' : '/test1/test2/test3', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'WEB адрес фронта МПП'},
                    {'path_to_el' : '//*[@id="settings_setup_field_web_address"]'},
                    {
                        'correct_test' :    [{ 'text' : 'https://111.111.111.111/test/', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Включить TLS для отправки сообщений'},
                    {'path_to_el' : '//*[@id="settings_setup_field_mail_send_enable_tls"]'},
                    {
                        'correct_test' :    [{ 'text' : 'false', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Режим работы модуля Криптографическая обработки данных'},
                    {'path_to_el' : '//*[@id="settings_setup_field_encryption_mode "]'},
                    {
                        'correct_test' :    [{ 'text' : '1', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Пользователь'},
                    {'path_to_el' : '//*[@id="settings_setup_field_mail_user"]'},
                    {
                        'correct_test' :    [{ 'text' : 'test@star.lanit.ru', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'Почтовый ящик'},
                    {'path_to_el' : '//*[@id="settings_setup_field_mail_box"]'},
                    {
                        'correct_test' :    [{ 'text' : 'test@star.lanit.ru', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Сервер Янтарь'},
                    {'path_to_el' : '//*[@id="settings_setup_field_amber_host"]'},
                    {
                        'correct_test' :    [{ 'text' : '111.111.111.111', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Имя сессии Янтарь'},
                    {'path_to_el' : '//*[@id="settings_setup_field_amber_cert_my"]'},
                    {
                        'correct_test' :    [{ 'text' : 'test001', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'Уровень логирования модуля Криптографическая обработка данных'},
                    {'path_to_el' : '//*[@id="settings_setup_field_crypto_logger_level"]'},
                    {
                        'correct_test' :    [{ 'text' : 'INFO', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                # (   {'test_name' : 'Пароль сессии Янтарь'},
                #     {'path_to_el' : '//*[@id="settings_setup_field_amber_cert_pass"]'},
                #     {
                #         'correct_test' :    [{ 'text' : 'INFO', 'status' : True }],
                #         'string' :          [{ 'text' : config.default_string, 'status': True }],
                #         'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                #         'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                #         'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                #     }
                # ),
                (   {'test_name' : 'Порт Янтарь'},
                    {'path_to_el' : '//*[@id="settings_setup_field_amber_port"]'},
                    {
                        'correct_test' :    [{ 'text' : '1333', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : '12345', 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Уровень логирования модуля Антивирусная проверка'},
                    {'path_to_el' : '//*[@id="settings_setup_field_antivir_logger_level"]'},
                    {
                        'correct_test' :    [{ 'text' : 'ALL', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Путь к KAV'},
                    {'path_to_el' : '//*[@id="settings_setup_field_antivirus_path"]'},
                    {
                        'correct_test' :    [{ 'text' : '/test/test', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Уровень логирования модуля Разархивирование'},
                    {'path_to_el' : '//*[@id="settings_setup_field_unzip_logger_level"]'},
                    {
                        'correct_test' :    [{ 'text' : 'ALL', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Входящй каталог'},
                    {'path_to_el' : '//*[@id="settings_setup_field_file_income_folder"]'},
                    {
                        'correct_test' :    [{ 'text' : '/test1/test2', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Исходящий каталог'},
                    {'path_to_el' : '//*[@id="settings_setup_field_file_outgoing_folder"]'},
                    {
                        'correct_test' :    [{ 'text' : '/test1/test2', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Режим работы модуля Получение данных'},
                    {'path_to_el' : '//*[@id="settings_setup_field_module_work_type"]'},
                    {
                        'correct_test' :    [{ 'text' : '1', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Уровень логирования модуля Получение данных'},
                    {'path_to_el' : '//*[@id="settings_setup_field_mailer_logger_level"]'},
                    {
                        'correct_test' :    [{ 'text' : 'ALL', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Сервер POP3/IMAP'},
                    {'path_to_el' : '//*[@id="settings_setup_field_mail_pop3/imap_host"]'},
                    {
                        'correct_test' :    [{ 'text' : 'test.test.test.ru', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': True }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : True }],
                    }
                ),
                (   {'test_name' : 'Порт POP3/IMAP'},
                    {'path_to_el' : '//*[@id="172.29.39.37Не определен"]//*[@id="settings_setup_field_mail_pop3/imap_port"]'},
                    {
                        'correct_test' :    [{ 'text' : '587', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : '12345', 'status' : True }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Почтовый протокол'},
                    {'path_to_el' : '[//*[@id="172.29.39.37Не определен"]//*@id="settings_setup_field_pop3/imap"]'},
                    {
                        'correct_test' :    [{ 'text' : '0', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
                (   {'test_name' : 'Уровень логирования модуля Расчет контрольных сумм'},
                    {'path_to_el' : '//*[@id="settings_setup_field_calccrc_logger_level"]'},
                    {
                        'correct_test' :    [{ 'text' : 'ALL', 'status' : True }],
                        'string' :          [{ 'text' : config.default_string, 'status': False }],
                        'integer' :         [{ 'text' : config.default_integer, 'status' : False }],
                        'empty' :           [{ 'text' : config.default_emptystr, 'status' : False }],
                        'special_char' :    [{ 'text' : config.default_special_char, 'status' : False }],
                    }
                ),
            ]

    save_but = '//*[@id="settings_setup_button_3"]'
    successfully_saved = '/html/body/div[2]/div/div/div[2]'

    def object_system(self, name_test, path, text, status):
        Logger(f'{config.indicator_test_page} {self.__report}').infolog
        Logger(f'{config.indicator_test_name} {name_test["test_name"]}').infolog
        Logger(f'{config.indicator_test_param} Тестовое значение {text}').infolog

        el = Find_element(driver = self._driver, path = path['path_to_el'], wtime = 10).by_xpath_to_be_visibility
        Logger(f'{config.indicator_test_step} Нашёл элемент').infolog

        previous_value = el.get_attribute('value')
        Logger(f'{config.indicator_test_step} Запомнил предыдущее значение').infolog

        el.click()
        Placeholder(driver = self._driver).clear_place(el = el)
        Logger(f'{config.indicator_test_step} Очистил поле').infolog

        Placeholder(driver = self._driver).char_by_char(el = el, text = text)
        Logger(f'{config.indicator_test_step} Ввел тестовые данные').infolog

        but_save = Find_element(driver = self._driver, path = self.save_but, wtime = 10).by_xpath_to_be_visibility
        if but_save.is_enabled() != status:
            name_screen = self.save_screen_shot
            allure.attach(self._driver.get_screenshot_as_png(), name='screen_shot', attachment_type=AttachmentType.PNG)
            Logger(f'{config.indicator_test_result_err} Кнопка сохранить не соответствует ожиданиям от теста. Кнопка {but_save.is_enabled()}, ожидалось {status}').errorlog
            Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
            assert but_save.is_enabled() == status

        if but_save.is_enabled() == True:
            but_save.click()
            Logger(f'{config.indicator_test_step} Нажал сохранить').infolog

            Find_element(driver = self._driver, path = self.successfully_saved, wtime = 10).by_xpath_to_be_visibility
            self.time_out_animation
            self._driver.refresh()
            self.time_out_after_refresh
            Logger(f'{config.indicator_test_step} Обновил страницу').infolog

            el = Find_element(driver = self._driver, path = path['path_to_el'], wtime = 10).by_xpath_to_be_visibility
            new_value = el.get_attribute('value')
            Logger(f'{config.indicator_test_step} Сравниваю значения до и после').infolog
            if new_value == text:
                Logger(f'{config.indicator_test_step} Новые значения сохранились').infolog
            else:
                name_screen = self.save_screen_shot
                allure.attach(self._driver.get_screenshot_as_png(), name='screen_shot', attachment_type=AttachmentType.PNG)
                Logger(f'{config.indicator_test_result_err} Новые значения не сохранились').errorlog
                Logger(f'{config.indicator_test_screen} Изображение: {name_screen}').errorlog
                assert new_value == text
            
            Logger(f'{config.indicator_test_step} Возвращаю начальные значения').infolog
            Placeholder(driver = self._driver).clear_place(el = el)
            Placeholder(driver = self._driver).char_by_char(el = el, text = previous_value)
            but_save = Find_element(driver = self._driver, path = self.save_but, wtime = 10).by_xpath_to_be_visibility
            but_save.click()
            Find_element(driver = self._driver, path = self.successfully_saved, wtime = 10).by_xpath_to_be_visibility
            time.sleep(1)
        else:
            Logger(f'{config.indicator_test_step} Нельзя нажать на кнопку сохранить').infolog
        
        Logger(f'{config.indicator_test_result_suc} Начальные значения сохранены').infolog



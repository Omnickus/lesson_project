# ===========================================================
# ============ ОЖИДАНИЯ =====================================
# ===========================================================
# Время ожидания свободное. Не привязано к каким либо событям.
time_out_free = 3
# Время ожидания разных анимаций
default_timeout_animation = 3
# Время ожидания после перезагрузки страницы
time_out_after_refresh = 8
# Общее время ожидания для WebDriverWait
default_timeout = 15
# Время ожидания функции dinamic_path. Ищет элемент на странице по тексту и возвращает xpath
time_out_new_jump = 5 # Время сна до новой попытки поиска элемента
jump_count = 3 # Количество попыток поиска

# Общая тестовая буквенная строка
default_string = 'AaBbCcMmNnOoGgUu'
# Общая тестовая числовая строка
default_integer = '1234567890'
# Общая тестовая строка c спец символами
default_special_char = '!@#$%^&*'
# Общая пустая строка
default_emptystr = ''
# Общий тестовый пользователь
default_user = 'default_user'
# Общий тестовый пароль
default_passwd = 'qwerty123'

# ===========================================================
# ============ ОТЧЁТЫ =======================================
# ===========================================================
# Каталог сохранения скриншотов
path_screen_shot = 'screenshot'
# расширение сохраняемых скриншотов
image_extension = 'png'
# Флаг создания docx отчёта (true/False)
flag_create_report = False
# ===========================================================
# ============ ЛОГИРОВАНИЕ ==================================
# ===========================================================
# Установить уровень логирования
log_level = 'INFO' # 'CRITICAL','ERROR','WARNING','INFO','DEBUG'
# Логгер
logger_name = 'MPP-SELENIUM' # Имя логгера
logger_file_name = 'mpp_selenium.log' # Имя файла с логами (будет создан в корне проета)
# Обёртка для декоратора логов
name_file_for_docx_report_from_log = 'docx_report_v1.docx' # Имя файла отчета
decorator_start_test = '==== НАЧАЛО ТЕСТА ===='
decorator_end_test = '==== КОНЕЦ ТЕСТА ===='
indicator_test_page = 'test_page:'
indicator_test_name = 'test_name:'
indicator_test_param = 'test_param:'
indicator_test_step = 'step:'
indicator_test_result_suc = 'result_suc:'
indicator_test_result_err = 'result_err:'
indicator_test_screen = 'screenshot:'

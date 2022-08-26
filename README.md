# Selenium Mpp V3
Данное приложение осуществляет проверку базового функционала приложения ППиП, это:
1) Создание/Редактирование/Удаление настроек, пользователей и тд
2) Проверка остановки/запусков микросервисов
3) Проверка инпутов на разные типы данных (строка, число, спец-символы, пустая строка)

# ОКРУЖЕНИЕ
python3.7 и выше

# КАК УСТАНОВИТЬ
python3 -m venv env
pip install -r requarements.txt

# ЗАПУСК ТЕСТОВ
pytest -vs [дополнительные параметры]

Пример:
pytest -vsm system --url https://172.78.45.33 --browser chrome --bv 104.0 --vnc True --logs False

Список параметров, которые могут быть переданы в тест:
  Путь до драйвера на вашей машине 
    --driver ~/drivers/chrome
  Браузер (opera, chrome, firefox)
    --browser opera
  Базовый URL тестируемого стенда
    --url https://127.0.0.1:80/
  URL до selenoid, если установлен
    --executor 127.0.0.1
  Трансляция теста в selenoid
    --vnc True
  Логирование в selenoid
    --logs True
  Запись видео selenoid"ом
    --videos False
  Версия браузера для selenoid
    --bv 104.0







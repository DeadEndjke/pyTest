# Общее описание программы

Программа предназначена для поиска координат адреса, который вводит пользователь. Программа получает данные с API dadata https://dadata.ru/api/suggest/address/

# Общее описание логики работы решения

При запуске программы создастся локальная база данных с именем "db.db" в которой хранятся данные о настройке поиска

Для запуска

`python -u main.py`

При запуске программы вас спросят, использовать уже существующий аккаунт или создать новый.

Если был выбран вариант "создать аккаунт" вас попросят ввести API_KEY, который находится в личном кабинете сервиса dadata и язык на котором адреса будут выводиться

Для получения API ключа и секретного ключа Вам необходимо зарегистрироваться в сервисе, после чего необходимые данные будут доступны в Вашем личном кабинете по ссылке: https://dadata.ru/profile/#info

Если был выбран вариант "выбрать уже существующий вариант", то все существующие аккаунты отобразятся на экране, после чего стоит выбрать нужный

Далее вводите адрес в произвольной форме и выбираете для которого нужно отобразить координаты

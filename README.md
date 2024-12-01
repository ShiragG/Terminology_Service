# Тестовое задание на написание сервиса терминологии и REST API к нему

1. Откройте терминал и скопируйте код:
```shell
git clone https://github.com/ShiragG/Terminology_Service.git
```

2. Проект написан на python 3.10
```shell
python3.10 -m venv .venv
```

3. Разрешите запуск скрипта activate и активируйте его
```shell
# chmod +x ./.venv/bin/activate && ./.venv/bin/activate 
```

4. Перейдите в корень проекта и установите зависимости
```shell
cd ./Terminology_Service && pip install -r requirements.txt
```

5. Перейдите в папку с проектом и создайте базу данных
```shell
cd ./terminology_service && ./manage.py migrate
```

6. Создайте суперпользователя
```shell
./manage.py createsuperuser 
```

7. Запустите сервер http://127.0.0.1:8000/
```shell
./manage.py runserver
```

Админка: http://127.0.0.1:8000/admin/

Документация API: http://127.0.0.1:8000/swagger-ui/
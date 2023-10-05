# Report system
Report system for iron mining industry.

Полное описание и ТЗ ниже. Проект выполнен частично (только backend).


Запуск:
- Клонировать репозиторий.
- В .env.txt убрать расширение txt и указать данные для postgres.
- Запустить команду "docker-compose up --build" из корня проекта. Сервис будет доступен по адресу "http://0.0.0.0:8000/api/v1".


Эндпоинты:
- http://127.0.0.1:8000/api/v1/registration - Post эндпоинт регистрации нового пользователя. Принимает данные формата "{"email": "email@email.com", "password": "12345"}".
- http://127.0.0.1:8000/api/v1/login - Post эндпоинт. Принимает данные формата "{"email": "email@email.com", "password": "12345"}". Возвращает пару токенов JWT, которые сохраняются в http-only cookie и при запросе эндпоинта требующего авторизации подставляет токен из cookie. Так что вручную подставлять не нужно. По умолчанию созданы 2 пользователя "email=test1@test.ru, password='12345'" и "email=test2@test.ru, password='12345'".
- http://127.0.0.1:8000/api/v1/add - Post эндпоинт для создания сырья и его составляющих. Принимает данные формата {"materials": {"название_сырья": {"iron_content": float, "silicon_content": float, "aluminum_content": float, "calcium_content": float, "sulfur_content": float, "upload_date": "day-month-year"}}}.
- http://127.0.0.1:8000/api/v1/report/month-year>(example 09-2023) - Get эндпоинт. Выводит отчет для каждого сырья с минимальными, максимальными и средними данными для каждого состовляющего сырья.


ТЗ:


![ALT TEXT](https://github.com/mrPechen/report_system/blob/main/%D1%82%D0%B7.png)




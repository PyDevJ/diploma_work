Дипломная работа: Доска объявлений (SB1)
=====================
Данная работа представляет собой backend-часть для сайта объявлений. 
Frontend-часть уже готова.
___
Бэкенд-часть проекта предполагает реализацию следующего функционала:
- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту (не обязательно).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.
___
## Запуск проекта
### Клонировать проект с GitHub
### Создать виртуальное окружение
* `python -m venv env`

### Активировать виртуальное окружение
* `env/Scripts/activate (Windows)`
* `source env/bin/activate (Linux, MacOS)`

### Установить зависимости
* `pip install -r skymarket\requirements.txt`

### Создать файл `.env` и записать в него переменные окружения по шаблону `.env.example`

### Создать базу данных
* `psql -U postgres`
* `CREATE DATABASE skymarket;`

### Применить миграции 
* `python skymarket\manage.py makemigrations`
* `python skymarket\manage.py migrate`

### Применить подготовленные фикстуры
* `python skymarket\manage.py loadall`
- Пользователь администратор: admin@skypro.ru, пароль: 111

### Запустить приложение
* `python skymarket\manage.py runserver`

### Доступ к backend с документацией API по адресу
* http://localhost:8000/api/swagger/
___

### Настройки Docker-compose
#### Создать файл `.env.docker` и записать в него переменные окружения по шаблону `.env.docker.example`
#### Команды для запуска
* `docker-compose build` - создать контейнеры docker
* `docker-compose up` - запустить контейнеры docker

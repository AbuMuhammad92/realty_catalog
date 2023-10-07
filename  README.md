# Каталог объектов недвижимости

Этот проект является каталогом объектов недвижимости с возможностью фильтрации и просмотра деталей каждого объекта.

## Начало работы

### Предварительные требования

- Python 3.6+
- PostgreSQL

### Установка и настройка

1. **Клонирование репозитория**

   ```bash
   git clone https://github.com/YourUsername/realty_catalog.git
   cd realty_catalog

Настройка виртуального окружения и установка зависимостей
bash
Copy code
python -m venv venv
source venv/bin/activate  # Для Windows используйте: venv\Scripts\activate
pip install -r requirements.txt
Настройка базы данных
Сначала создайте базу данных в PostgreSQL. Затем примените структуру базы данных, используя:
bash
Copy code
psql -U your_username -d your_database_name -a -f database_setup.sql
Замените your_username на имя вашего пользователя PostgreSQL и your_database_name на имя вашей базы данных.
Запуск приложения
Установите переменные окружения:
bash
Copy code
export FLASK_APP=app.py
export FLASK_ENV=development
Запустите приложение:
bash
Copy code
flask run
Приложение теперь доступно по адресу http://127.0.0.1:5000.
Автор

Ваше имя



## Настройка базы данных

1. Создайте новую базу данных PostgreSQL.
2. Примените структуру базы данных и добавьте тестовые данные, используя следующую команду:
psql -U your_username -d your_database_name -a -f database_setup.sql

go
Copy code
Замените `your_username` на имя вашего пользователя PostgreSQL и `your_database_name` на имя вашей базы данных.


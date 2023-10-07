Этот проект представляет собой каталог объектов недвижимости с функциями фильтрации и просмотра деталей каждого объекта.

Предварительные требования
Python 3.6+
PostgreSQL
Установка и настройка

Клонирование репозитория:
bash
git clone https://github.com/AbuMuhammad92/realty_catalog.git
cd realty_catalog

Настройка виртуального окружения и установка зависимостей:
bash
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
pip install -r requirements.txt

Настройка базы данных:
Создайте новую базу данных в PostgreSQL.

Примените структуру базы данных, используя:
bash
psql -U your_username -d your_database_name -a -f database_setup.sql
Замечание: Замените your_username на имя вашего пользователя PostgreSQL и your_database_name на имя вашей базы данных.

Установка переменных окружения и запуск приложения:
bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
После запуска приложения перейдите к адресу: http://127.0.0.1:5000/.

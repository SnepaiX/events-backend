# Сервис для проведения мероприятий

Сервис для управления мероприятиями и местами их проведения.

## Стэк

- Python
- Django
- Django REST Framework
- PostgreSQL / SQLite
- Celery
- Redis
- OpenPyXL
- drf-spectacular

## Полностью выполнены

- CRUD для площадок проведения
- CRUD для мероприятий
- Поиск, сортировка и фильтрация для площадок и мероприятий
- Разграничение прав доступа
- Excel экспорт
- Документация в Swagger

## Частично выполнены

- Картинки для мероприятий
- Excel импорт

## Документация API и страница Админа

- http://127.0.0.1:8000/api/docs/
- http://127.0.0.1:8000/admin/

## Локальная установка

```bash
git clone https://github.com/SnepaiX/events-backend.git
cd project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

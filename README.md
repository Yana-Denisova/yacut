# Проект YaCut

## Ключевые возможности сервиса:
-генерация коротких ссылок и связь их с исходными длинными ссылками
-переадресация на исходный адрес при обращении к коротким ссылкам
-web интерфейсом и REST API

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Автор проекта](#Автор-проекта)

## Технологии
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Jinja](https://jinja.palletsprojects.com/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/)

## Использование

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/Yana-Denisova/yacut.git
SSH: git@github.com:Yana-Denisova/yacut.git
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
Проект использует базу данных SQLite.  
Для подключения и выполненя запросов к базе данных необходимо создать и заполнить файл ".env" с переменными окружения в корневой папке проекта.

Шаблон для заполнения файла ".env":

```python
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///yacut_db.sqlite3
SECRET_KEY='Здесь указать секретный ключ'
Создать базу данных и выполнить миграции:

```bash
flask db upgrade
```

Запустить проект можно командой:
```bash
flask run
```

web интервейс будет доступен по адрес [http://localhost:5000/](http://localhost:5000/)

---

## Автор проекта:

- [Денисова Яна](https://t.me/DenisovaYana)

# 🚀 TaskTime

Hello, I started developing this project with the goal that it will one day become quite popular for people who need to plan their time. At the moment, it is released as an MVP on Flask.

## 🧰 Prerequisites
- Python(3.10 version)

## 🧩 Dependencies

I'm using the **Flask** framework as the core of the app, it's an MVP app, so good old Flask seemed like a good choice

## ⚙️ Installation 

If someone wants to test my API or improve it, I wrote a guide for installation, after a while a section will be added describing what and how it works in the project so that you don't have to deal with 0

1. First run the command in the terminal: ```git clone https://github.com/Evgen-Jekov/TaskTime```

2. Then create .venv with this command in the terminal: ```python -m venv venv```

3. Once you have created .venv activate it, here are the commands in the terminal for Windows, Linux(MacOS):

    **Windows:** 
    ```venv\Scripts\activate.bat```

    **Linux(MacOS):** 
    ```source venv/bin/activate```

4. Now all that's left to do is just write in the console after activation:

    ```pip install -r requirements.txt```

5. Then create .env and .flaskenv. 

    **In .env write:** 
    `DB = sqlite:///test.db`

    This is an example, you can connect any relational database, the only condition is that it must be supported by SQLAlchemy

    **In .flaskenv write:**
    `FLASK_APP=main.py`

    Using FLASK_APP=main.py in .flaskenv we tell the terminal where to look for our flask application to work with the terminal, for example we will use it to apply migrations

## 📦 Migrations

for migrations I used Flask-Migrate, you can find the instructions on how to use it at this link:

`https://flask-migrate.readthedocs.io/en/latest/`

## 📃 instructions what works in the project

Let's start with the fact that the project is built on SOLID principles (at least I tried to do it) and let me add that the work with the user is not added yet, and probably will not be added at all, I can not be sure who will want to work with the user, and so I prefer to leave this part for those enthusiasts who may decide to work with my project. now let's go through the layers of my application that how it is organized.

Let's start with the project structure itself, where all the files are shown in expanded form:

```
├── api
│   ├── app
│   │   ├── connect
│   │   │   ├── connector.py
│   │   │   ├── connector_route.py
│   │   │   └── __pycache__
│   │   │       ├── connector.cpython-310.pyc
│   │   │       └── connector_route.cpython-310.pyc
│   │   ├── core
│   │   │   ├── extensions.py
│   │   │   └── __pycache__
│   │   │       └── extensions.cpython-310.pyc
│   │   ├── model
│   │   │   ├── category_model.py
│   │   │   ├── __pycache__
│   │   │   │   ├── category_model.cpython-310.pyc
│   │   │   │   ├── database.cpython-310.pyc
│   │   │   │   ├── task_model.cpython-310.pyc
│   │   │   │   └── timer_model.cpython-310.pyc
│   │   │   ├── task_model.py
│   │   │   └── timer_model.py
│   │   ├── repository
│   │   │   ├── add.py
│   │   │   ├── auxiliary.py
│   │   │   ├── category.py
│   │   │   ├── database_abc.py
│   │   │   ├── __pycache__
│   │   │   │   ├── add.cpython-310.pyc
│   │   │   │   ├── auxiliary.cpython-310.pyc
│   │   │   │   ├── BaseDB.cpython-310.pyc
│   │   │   │   ├── category.cpython-310.pyc
│   │   │   │   ├── database_abc.cpython-310.pyc
│   │   │   │   ├── task.cpython-310.pyc
│   │   │   │   └── timer.cpython-310.pyc
│   │   │   ├── task.py
│   │   │   └── timer.py
│   │   ├── route
│   │   │   ├── category_route.py
│   │   │   ├── __pycache__
│   │   │   │   ├── category_route.cpython-310.pyc
│   │   │   │   ├── task_route.cpython-310.pyc
│   │   │   │   └── timer_route.cpython-310.pyc
│   │   │   ├── task_route.py
│   │   │   └── timer_route.py
│   │   ├── schemes
│   │   │   ├── category_schemes.py
│   │   │   ├── __pycache__
│   │   │   │   ├── category_schemes.cpython-310.pyc
│   │   │   │   ├── task_schemes.cpython-310.pyc
│   │   │   │   └── timer_schemes.cpython-310.pyc
│   │   │   ├── task_schemes.py
│   │   │   └── timer_schemes.py
│   │   ├── serialization
│   │   │   ├── __pycache__
│   │   │   │   └── serialization.cpython-310.pyc
│   │   │   └── serialization.py
│   │   └── service
│   │       ├── __pycache__
│   │       │   ├── service_abc.cpython-310.pyc
│   │       │   └── service.cpython-310.pyc
│   │       ├── service_abc.py
│   │       └── service.py
│   ├── config.py
│   ├── create_app.py
│   ├── instance
│   │   └── TaskTime.db
│   ├── main.py
│   ├── migrations
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── __pycache__
│   │   │   └── env.cpython-310.pyc
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 855f8ca66b33_task_category_and_timer_create.py
│   │       └── __pycache__
│   │           └── 855f8ca66b33_task_category_and_timer_create.cpython-310.pyc
│   └── __pycache__
│       ├── config.cpython-310.pyc
│       ├── create_app.cpython-310.pyc
│       └── main.cpython-310.pyc
├── README.md
└── requirements.txt
```

## ✍️ Author

the author of the project is Zhekov Evgen, I hope someone will find it interesting, in any case if you read the README I am grateful to you ❤️
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
.
├── api
│   ├── app
│   │   ├── connect
│   │   │   ├── connector.py
│   │   ├── core
│   │   │   ├── extensions.py
│   │   ├── model
│   │   │   ├── category_model.py
│   │   │   ├── task_model.py
│   │   │   ├── timer_model.py
│   │   │   └── user_model.py
│   │   ├── repository
│   │   │   ├── add.py
│   │   │   ├── auxiliary.py
│   │   │   ├── category.py
│   │   │   ├── database_abc.py
│   │   │   ├── task.py
│   │   │   ├── timer.py
│   │   │   └── user.py
│   │   ├── route
│   │   │   ├── category_route.py
│   │   │   ├── task_route.py
│   │   │   ├── timer_route.py
│   │   │   └── user_route.py
│   │   ├── schemes
│   │   │   ├── category_schemes.py
│   │   │   ├── task_schemes.py
│   │   │   ├── timer_schemes.py
│   │   │   └── user_schemas.py
│   │   ├── serialization
│   │   │   └── serialization.py
│   │   └── service
│   │       ├── service_abc.py
│   │       └── service.py
│   ├── config.py
│   ├── create_app.py
│   ├── main.py
├── README.md
└── requirements.txt
```

Next, let's talk about which layers are responsible for what:

- connect - this layer contains a class for connecting dependencies and routes of our API, the class name is Connector (it inherits from the Connect class).

- core - Here are all dependencies that we connect to our application, for now there are not many, but in the future will be more.

- model - Here are the models for working with the database through SQLAlcgemy, the models are not complicated, it will be easy to understand them

- repository - The most interesting thing for me is that the repository contains our classes for low-level work with the database, these classes are inherited from interfaces (look for them in the database_abc.py file).

- route - All routes of our application are collected here, they are as simple as possible due to the fact that they are only responsible for creating the necessary objects for working with services (we will get to them yet), so we will not dwell on them for long.

- schemes - here is the storage of schemes for input data validation, they are based on our models (see models folder).

- serialization - Although there is only one file here, but it is not less important, it describes classes for serialization and deserialization of our json or database objects through interfaces.

- service - This is almost the main part of the process, with the help of class interfaces we create services that are as flexible as possible and can work with all operations, without paying attention to what database object is being worked with.

- instance, migrations - These are folders created by libraries, you will have the same after installation and customization, also they are not added to the repository, so you can't look at them. 

- .flaskenv - This is a file created so that you don't have to set the flask variable in the terminal every time to work with the CLI, you just need to write this in the file: 

    `FLASK_APP=main.py`

- config.py - this file has a class config, it is used to set the necessary configs for our application Flask through the method from_object

- create_app.py - there is only one function that creates our Flask application and connects everything needed to it

- main.py - through this file we launch our application

## 🎯 plans for the future

1. create a mechanism for working with the user
4. add data analytics to a project

## ✍️ Author

the author of the project is Zhekov Evgen, I hope someone will find it interesting, in any case if you read the README I am grateful to you ❤️
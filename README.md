# TaskTime

Hello, I started developing this project with the goal that it will one day become quite popular for people who need to plan their time. At the moment, it is released as an MVP on Flask.

## Prerequisites
- Python(3.10 version)

## Dependencies

I'm using the Flask framework as the core of the app, it's an MVP app, so good old Flask seemed like a good choice

## Install 

If someone wants to test my API or improve it, I wrote a guide for installation, after a while a section will be added describing what and how it works in the project so that you don't have to deal with 0

1. First run the command in the terminal: ```https://github.com/Evgen-Jekov/TaskTime```

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
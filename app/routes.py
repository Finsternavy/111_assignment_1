from flask import Flask

app = Flask(__name__)


@app.get("/")
def helloWorld():
    return "<h1>Hello, world!</h1>"

@app.get("/about")
def get_about():
    me = {
        "first_name": "Chris",
        "last_name": "Finster",
        "hobbies": "Escaping from Tarkov",
        "active": True
    }
    return me
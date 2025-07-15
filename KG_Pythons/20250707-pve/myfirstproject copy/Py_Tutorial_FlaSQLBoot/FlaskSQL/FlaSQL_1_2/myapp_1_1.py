# Flask + SQLite3 + Bootstrap
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return "Hello, World!"

@app.route('/add')
def add_employee():
    return "Add members here."

if __name__ == '__main__':
    app.run()
from flask import Flask,redirect,url_for,render_template
import config
from test import hello

app = Flask(__name__)
app.config.from_object(config)
import jinja2

@app.route('/')
def hello_world():

    return render_template('home.html')






if __name__ == '__main__':
    app.run()
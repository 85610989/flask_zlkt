from flask import Flask,url_for,render_template,redirect
import config


app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

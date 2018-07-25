from flask import Flask,redirect,url_for,render_template
import config


app = Flask(__name__)
app.config.from_object(config)
import jinja2

@app.route('/')
def hello_world():
    #return redirect(url_for('article',id=123))
    context = {
        'username':'jiangzhipeng',
        'gender':'男',
        'age':18
    }
    return render_template('index.html', **context)

@app.route('/login/')
def article():
     #return '你请求的参数是:%s' % id
    return render_template('test.html')


@app.route('/question/<is_login>/')
def question(is_login):
    if is_login == '1':
        return '您已经登录'
    else:
        return '您没有登录'




if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
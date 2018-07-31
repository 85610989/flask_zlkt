from flask import Flask,redirect,url_for,render_template,request
import config
from fuction import average_capital_plus_interest,average_capital,equal_capital_equal_interest,interest_first_then_capital

app = Flask(__name__)
app.config.from_object(config)
import jinja2

@app.route('/',methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        money=int(request.form['money'])
        rate=float(request.form['rate'])/100
        term=int(request.form['term'])
        repayStyle=request.form['repayMethod']
        if repayStyle =='等额本息':

            debx=average_capital_plus_interest(money,rate,term)
            return render_template('result.html',debx=debx,term=term)
        if repayStyle =='等额本息':
            return render_template('result.html')
        if repayStyle =='等额本息':
            return render_template('result.html')
        if repayStyle =='等额本息':
            return render_template('result.html')
        else:
            return '请输入正确的选择'







if __name__ == '__main__':
    app.run()
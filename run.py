# -*- coding:utf-8 -*- 

from flask import Flask,redirect,url_for,render_template,request
import config
from fuction import average_capital_plus_interest,average_capital,equal_capital_equal_interest,interest_first_then_capital,quarter_interest_first_then_capital

app = Flask(__name__)
app.config.from_object(config)
import jinja2

@app.route('/',methods=['GET', 'POST'])
def hello_man():
    try:
        if request.method == 'GET':
            return render_template('home.html')
        else:
            money=int(request.form['money'])
            rate=float(request.form['rate'])/100
            term=int(request.form['term'])
            repayStyle=request.form['repayMethod']
            if repayStyle =='等额本息':
                debx=average_capital_plus_interest(money,rate,term)
                return render_template('result.html',repayMethod=debx)
            if repayStyle =='等额本金':
                debj=average_capital(money,rate,term)
                return render_template('result.html',repayMethod=debj)
            if repayStyle =='等本等息':
                dbdx=equal_capital_equal_interest(money,rate,term)
                return render_template('result.html',repayMethod=dbdx)
            if repayStyle =='按月还息到期还本':
                axhxdqhb=interest_first_then_capital(money,rate,term)
                return render_template('result.html',repayMethod=axhxdqhb)
            if repayStyle =='按季还息到期还本':
                ajhxdqhb=quarter_interest_first_then_capital(money,rate,term)
                return render_template('result.html',repayMethod=ajhxdqhb)
    except Exception:
        return render_template('warn.html')


@app.route('/vip/',methods=['GET', 'POST'])
def hello_vip():
    try:
        if request.method == 'GET':
            return render_template('home.html')
        else:
            money=int(request.form['money'])
            rate=float(request.form['rate'])/100
            term=int(request.form['term'])
            repayStyle=request.form['repayMethod']
            if repayStyle =='等额本息':
                debx=average_capital_plus_interest(money,rate,term)
                return render_template('vip_result.html',repayMethod=debx)
            if repayStyle =='等额本金':
                debj=average_capital(money,rate,term)
                return render_template('vip_result.html',repayMethod=debj)
            if repayStyle =='等本等息':
                dbdx=equal_capital_equal_interest(money,rate,term)
                return render_template('vip_result.html',repayMethod=dbdx)
            if repayStyle =='按月还息到期还本':
                axhxdqhb=interest_first_then_capital(money,rate,term)
                return render_template('vip_result.html',repayMethod=axhxdqhb)
            if repayStyle =='按季还息到期还本':
                ajhxdqhb=quarter_interest_first_then_capital(money,rate,term)
                return render_template('vip_result.html',repayMethod=ajhxdqhb)
    except Exception:
        return render_template('warn.html')


if __name__ == '__main__':
    app.run()
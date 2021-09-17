'''
used redirect & url route feature
used jinja 2 template techniques
{% %} for looping purpose
{# #} for comment purpose
{{ variable }} for rendering variable value
'''

from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('mark.html')

@app.route("/result/<int:score>")
def result(score):
    result = ""
    if score >= 50:
        result = 'sucess'
    else:
        result = 'fail'
    return redirect(url_for(result,score=score))


@app.route("/submit", methods=['POST', 'GET'])
def submit():

    second_turm=int(request.form['second_turm'])
    first_turm=int(request.form['first_turm'])
    result =""
    score = (second_turm+first_turm)/2
    if score >= 50:
        result ='sucess'
    else:
        result = 'fail'
    return redirect(url_for(result,score=score))

@app.route("/pass/<int:score>")
def sucess(score):
    msg="pass"
    result=" you passed with {}".format(score)
    return render_template('result.html', msg=msg, result=result)

@app.route("/fail/<int:score>")
def fail(score):
    msg = " better luck next time :) score {}".format(score)
    result = 'fail'
    return render_template('result.html',msg=msg,result=result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

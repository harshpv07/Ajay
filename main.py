from flask import Flask, url_for,render_template,request
from search import *

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('front.html' , data = getresult(request.form['sea']))
    return render_template('front.html')


if __name__ == '__main__':
    app.run(debug= True)
import pyrebase
config = {
    "apiKey": "AIzaSyCb83GlcTfsc08RxPAkmgDg1dqS3HFzj9U",
    "authDomain": "search-9f0c4.firebaseapp.com",
    "databaseURL": "https://search-9f0c4.firebaseio.com",
    "projectId": "search-9f0c4",
    "storageBucket": "search-9f0c4.appspot.com",
    "messagingSenderId": "905820569650"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


from flask import Flask,render_template,url_for,request
from search import *


app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('front.html' , data = getresult(request.form['sea']))
    return render_template('front.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup',methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        uname = request.form['user']
        pas = request.form['pass']
        db.child('sign').push({uname:pas})
        temp = db.child('sign').get()
        tempo = temp.val()
        return render_template('signup.html',t = tempo.values())
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug= True)
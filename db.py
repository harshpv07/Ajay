import pyrebase
config = {
    apiKey: "AIzaSyCb83GlcTfsc08RxPAkmgDg1dqS3HFzj9U",
    authDomain: "search-9f0c4.firebaseapp.com",
    databaseURL: "https://search-9f0c4.firebaseio.com",
    projectId: "search-9f0c4",
    storageBucket: "search-9f0c4.appspot.com",
    messagingSenderId: "905820569650"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database

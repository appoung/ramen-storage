import pyrebase
config = {
        "apiKey": "AIzaSyD_5moavP8FIt5YZV9QebLv7uDQ-zQ3Hxg",
        "authDomain": "ramen-storage.firebaseapp.com",
        "databaseURL": "https://ramen-storage-default-rtdb.firebaseio.com",
        "projectId": "ramen-storage",
        "storageBucket": "ramen-storage.appspot.com",
        "messagingSenderId": "887325871160",
        "appId": "1:887325871160:web:d4a156e8eeb814420deacd"
        }
firebase = pyrebase.initialize_app(config)
db = firebase.database()
users = db.child("id").get()
print(users.val())
def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote

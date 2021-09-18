from website import create_app
import pyrebase

app = create_app()

config = {
    'apiKey': "AIzaSyAdNWl10pzwhawDFR-pKvXgJ_jz24j9pHI",
    'authDomain': "space-667e4.firebaseapp.com",
    'projectId': "space-667e4",
    'storageBucket': "space-667e4.appspot.com",
    'messagingSenderId' : "403454559792",
    'appId' : "1:403454559792:web:7f73a741c1ba2b0c194ff5",
    'measurementId' : "G-W0P1BRD9G0"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

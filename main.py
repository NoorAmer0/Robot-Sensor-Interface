from flask import Flask,render_template,request
import pyrebase
from datetime import datetime
config = {
  "apiKey": "",
  "authDomain": "sensorstore-36ab5.firebaseapp.com",
  "databaseURL": "https://sensorstore-36ab5-default-rtdb.firebaseio.com",
  "storageBucket": ""
}
firebase = pyrebase.initialize_app(config)
app = Flask(__name__)



@app.route("/" ,methods=['GET'])
def getValue():
    if request.args.get('num'):
        val = request.args.get('num')
        ts = datetime.now().strftime("%d_%m_%Y, %H:%M:%S")
        firebase.database().child(ts).set(val)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()


# Task_3_summer_Training
This projrects explains how I used Flask microframework in Python to create a dynamic web page that uses HTTP GET method to get an input from sensor and store it in Firebase realtime databse along with the timestamp of this input.

### Prerequisite:
1-Install Python.

2-PyCharm IDE.

3-Install Flask.

4-Firebase account.

### Steps:
1-create a simple `HTML` page that contains a `form` tag, make sure that you used the `name` attribute of the input tags:

```    <form action="{{url_for('getValue')}}" method="get">
      <label>Sensor value is:</label>
      <input type="number" placeholder="value" name="num">
      <input value="send" type="submit" name="sent">
    </form>
``` 
the code between curly brackets is a `Jinja code`, or Python inside HTML code, that switch the implementation to Python file `getValue` method that will store the data inside the database.

Look at the page:

![2022-07-31 (2)](https://user-images.githubusercontent.com/73133501/182040044-0e9bbc1c-dd0a-4a65-bfe3-d8b01b17ecb0.png)


2-In `main.py` we will import three libraries:

```

from flask import Flask,render_template,request
import pyrebase
from datetime import datetime

```
`pyrebase` is a simple python interface for the Firebase API, it is better than `firebase-admin` in term of easiness, BUT, be carefull that we will install `pyrebase4` which is the consistant version of this library, otherwise you will fell in endless errors.

`pyrebase4` on github here: https://github.com/nhorvath/Pyrebase4

3-In our firebase tree structre database, we will have two things: key and child, each key will store the `timestamp` which is the date along with the time, so each value will be unique.

```

@app.route("/" ,methods=['GET'])
def getValue():
    if request.args.get('sent') == 'send':
        val = request.args.get('num')
        ts = datetime.now().strftime("%d_%m_%Y, %H:%M:%S")
        firebase.database().child(ts).set(val)
    return render_template("index.html")

```

4-We have only one page, or in Flask terms only on `route`, so under this route in `main.py` file we will initialize our `getValue` method that will return the html page, or will be linked to its template `index.html`.

`if request.args.get('sent') == 'send':` if the user clicked on send button and the `url` contains the value of `sent=send` then do the next.

`val = request.args.get('num')` store the input value, that is currently in the `url` with the argumnt `num`

`ts = datetime.now().strftime("%d_%m_%Y, %H:%M:%S")` store the timestamp as String, and modify its format as `dd_mm_yyyy`, so it can be appended in the `url` without problem.

`firebase.database().child(ts).set(val)` set the value of the variable `val` under the chiled `ts` which is under the root of this tree which represent the database as a whole.

#### INPUT:
![2022-07-31 (1)](https://user-images.githubusercontent.com/73133501/182041105-062715f4-8c55-4aff-ba7d-a08f84710486.png)

#### ~~~~~~~~ #####

#### DATABASE:
![2022-07-31 (3)](https://user-images.githubusercontent.com/73133501/182041053-8f3e5600-709a-49ae-b8f1-78a3fe4ac2fd.png)


### Note:

I think that using `POST` method with this application is bettre than 'GET', it is not about how much these data are secure, but it is about HTTP protocole, if we inputted a value then the `url` of the page will change as a result, then if the user for any reason `refresh` the page incorrect input will be submitted to the database.
`GET` is used to get an object the sent information is about the requested object, while `POST` is used to send a data that will be stored in a database.

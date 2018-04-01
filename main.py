from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')



@app.route("/", methods=['POST'])
def welcome():

    username = request.form['username']

    if len(username) > 20:
        return 'error'

    else:
        return '<h1>Welcome ' + username + '</h1>'



app.run ()
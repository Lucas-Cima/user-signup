from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')



@app.route("/", methods=['POST', 'GET'])
def welcome():

    username = request.form['username']
    username_error = ''



    if len(username) > 20:
        return 'error'

    else:
        return render_template('welcome.html', username=username)



app.run ()
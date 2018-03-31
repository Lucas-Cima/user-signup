from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/")
def index():
    return 



@app.route("/", methods=['POST'])
def welcome():
    return



from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def display_user_signup():
    return render_template('index.html')




@app.route("/", methods=['POST', 'GET'])
def validate_signup():       
    username = request.form['username']
    username_error = ''
    
    if len('username') > 20 or len('username') < 3:
        username_error = 'Not a Valid Username'
        username = ''
    else:
        return render_template('index.html', username=username, username_error=username_error)





#@app.route("/welcome", methods=['POST', 'GET'])
#def welcome():
    #username = request.args.get('username')

    #return render_template('welcome.html', username=username)



app.run ()
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup", methods=['GET'])
def display_user_signup():
    return render_template('index.html')




@app.route("/signup", methods=['POST'])
def validate_signup():       
    username = request.form['username']
    username_error = ''
    password = request.form['password']
    password_error = ''
    verify = request.form['verify']
    verify_error = ''
    email = request.form['email']
    email_error = ''
    
    if len(username) > 20 or len(username) < 3:
        username_error = 'Not a Valid Username'

        return render_template('index.html', username_error=username_error, password_error=password_error, 
        verify_error=verify_error, email_error=email_error)


    else:
        return redirect("/welcome?username={0}".format(username))




@app.route("/welcome", methods=['POST', 'GET'])
def welcome():
    username = request.args.get('username')

    return render_template('welcome.html', username=username)



app.run ()
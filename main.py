from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['GET'])
def display_user_signup():
  

    return render_template('index.html')




@app.route("/", methods=['POST'])
def validate_signup():       
    username = request.form['username']
    username_error = ''
    password = request.form['password']
    password_error = ''
    verify = request.form['verify']
    verify_error = ''
    email = request.form['email']
    email_error = ''
    
    if len(username) > 20 or len(username) < 3 or ' ' in username:
        username_error = 'Not a Valid Username'
    
    if len(password) > 20 or len(password) < 3 or ' ' in password:
        password_error = 'Not a Valid Password'
    
    if verify != password:
        verify_error = 'Passwords do Not Match'

    if len(email) > 1:
        if "@" and "." not in email or len(email) > 20 or len(email) < 3 or ' ' in email:
            email_error = 'Not a Valid E-mail'

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect("/welcome?username={0}".format(username))
    
    
    else:
        return render_template('index.html', username_error=username_error, password_error=password_error, 
        verify_error=verify_error, email_error=email_error, form=request.form)




@app.route("/welcome", methods=['POST', 'GET'])
def welcome():
    username = request.args.get('username')

    return render_template('welcome.html', username=username)



app.run ()
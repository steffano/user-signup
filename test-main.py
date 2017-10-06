from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')
def PWD_USR_VALID(user_input):
    if len(user_input) < 4 or len(user_input) > 20 or ' ' in user_input:
        return False 

def Email_Valid(email_input):
    if PWD_USR_VALID(email_input) or len(email_input) < 3 or len(email_input) > 20 in email_input or '@' not in email_input or '.' not in email_input:
        return False


@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    verify = request.form['verify']

    if PWD_USR_VALID(username) == False:
        username_error = "Please enter a valid username"
        return render_template('signup.html', username_error=username_error, username=username, email=email)

    if PWD_USR_VALID(password) == False:
        password_error = "Please enter a valid password"
        return render_template('signup.html', password_error=password_error, username=username, email=email)

    if password != verify:
        verify_error = "Your passwords don't match, please try again"
        return render_template('signup.html', verify_error=verify_error, username=username, email=email)

    if len(email) >= 1:
        if Email_Valid(email) == False:
            email_error = "Please enter a valid email"
            return render_template('signup.html', email_error=email_error, username=username, email=email)

    return render_template("welcome.html", username=username)

app.run()
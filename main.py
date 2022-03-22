from flask import Flask, render_template, request
from forms import LoginForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "appsecretkey"


@app.route("/")
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        right_email = "admin@email.com"
        right_password = "12345678"
        if login_form.email.data == right_email and login_form.password.data == right_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
key = os.environ.get('API_SECRET')
class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), validators.Length(min=6, max=200), validators.Email()])
    password = PasswordField(label='password', validators=[DataRequired(), validators.Length(min=8, max=20)])
    submit = SubmitField(label='Log In')

app = Flask(__name__)
Bootstrap(app)
app.secret_key = key






@app.route("/")
def home():
    return render_template('index.html')
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)

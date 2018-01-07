from flask import Flask, request, redirect, render_template
# from wtforms import Form, BooleanField, StringField, PasswordField, validators
# import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/' methods="GET")
@app.route('/index', methods="GET")
def index():
    return render_template("base.html")


@app.route('/welcome {{user}}', methods="POST")
def welcome():
    return render_template(welcome.html)


if __name__ == '__main__':
    app.run()

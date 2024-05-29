from .utils import auth_required                                                                                                          
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template("simple.html")

@app.route('/hello')
def hello():
    return "Hello, World!"


@app.route('/user')
def get_user():
    name = request.args.get('name')
    return "Requested for name = %s" % name

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    return "Login successful for %s:%s" % (username, password)


@app.route('/save', methods=['POST'])
def save_user():
    user_data = request.json
    return 'Saving user with id = %d' % (user_data.get('id'))


@app.route('/secret')
@auth_required
def secret_view():
    return render_template("secret.html")

app.run(port=3000)

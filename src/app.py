from flask import Flask
from src.utils import *
app = Flask(__name__)


@app.route('/')
def hello():
    return "Venmo App!"


@app.route('/api/v1/check_balance/<name>')
def test(name):
    return str(check_balance(user= name))

# @app.route('/api/v1/list_users/recieve_from_list/<name>')
# recieve_from_list()

# @app.route('/api/v1/list_users/to_send_list/<name>')
# to_send_list()

@app.route('/api/v1/list_users/transfer_list/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
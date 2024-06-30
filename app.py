from flask import Flask, jsonify
from models import db, User
import os

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

if __name__ == '__main__':
    app.run()

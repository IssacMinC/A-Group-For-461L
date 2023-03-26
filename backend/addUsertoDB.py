from pymongo import MongoClient
import certifi
import cipher

from flask import Flask, redirect, url_for, request, render_template, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})
#CORS(app)


ca = certifi.where()

@app.route('/')
def index():
    return "Hello, World!"

# @app.route('/signup', methods=['GET'])
# def queryHWSet1Availability():
#     client = MongoClient("mongodb+srv://asamant:EE461LSp23@cluster0.oovet.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)

#     db = client.HardwareSet

#     set1 = db.HWSet1

#     query = {"Description": "Hardware Set 1"}
#     x = set1.find_one(query)
#     avail = x["Availability"]
#     client.close()
#     return str(avail)


@app.route('/signup/<username>/<password>', methods=['POST'])
def addNewUser(username, password):
    

    client = MongoClient("paste team DB link here", tlsCAfile=ca)

    db = client["Users"]
    collection_name = db['users']

    checkExistingUser = collection_name.find_one({"userId": username})

    if checkExistingUser:
        response = jsonify({'msg': 'User Already Exists'})
        response.headers.set('Access-Control-Allow-Origin', '*')
        return response

    encryptedPassword = cipher.encrypt(password, 3, 1)

    userDoc = {
        "userId": username,
        "password": encryptedPassword
    }

    collection_name.insert_one(userDoc)
    client.close()

    response = jsonify({'msg': 'User Created'})
    response.headers.set('Access-Control-Allow-Origin', '*')
    return response

@app.route('/login/<username>/<password>', methods=['POST'])
def login(username, password):
    client = MongoClient("paste team DB link here", tlsCAfile=ca)

    db = client["Users"]
    collection_name = db['users']

    checkUserPassword = collection_name.find_one({"userId": username, "password": cipher.encrypt(password, 3, 1)})

    if not checkUserPassword:
        response = jsonify({'msg': 'Invalid Username or Password'})
        response.headers.set('Access-Control-Allow-Origin', '*')
        return response
    else:
        response = jsonify({'msg': 'Login Successful'})
        response.headers.set('Access-Control-Allow-Origin', '*')
        return response

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
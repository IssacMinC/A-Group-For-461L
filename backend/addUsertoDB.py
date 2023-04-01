from pymongo import MongoClient
import certifi
import cipher

from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})


ca = certifi.where()

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/signup/<username>/<password>', methods=['POST'])
def addNewUser(username, password):
    

    client = MongoClient("mongodb+srv://test:2cinKpO1locYEb76@cluster1.wjept6s.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)

    db = client["User"]
    collection_name = db["Users"]

    checkExistingUser = collection_name.find_one({"userId": username})

    if checkExistingUser:
        response = jsonify({'msg': 'User Already Exists'})
        response.headers.set('Access-Control-Allow-Origin', '*')
        return response

    encryptedPassword = cipher.encrypt(password, 3, 1)
    
    projectArray = []

    userDoc = {
        "UserId": username,
        "Password": encryptedPassword,
        "ProjectID": projectArray
    }

    collection_name.insert_one(userDoc)
    client.close()

    response = jsonify({'msg': 'User Created'})
    response.headers.set('Access-Control-Allow-Origin', '*')
    return response

@app.route('/login/<username>/<password>', methods=['POST'])
def login(username, password):
    client = MongoClient("mongodb+srv://test:2cinKpO1locYEb76@cluster1.wjept6s.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)

    db = client["User"]
    collection_name = db["Users"]

    checkUserPassword = collection_name.find_one({"UserId": username, "Password": cipher.encrypt(password, 3, 1)}, {"ProjectID": 0})
    client.close()
    
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
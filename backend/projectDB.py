from pymongo import MongoClient
import certifi
from flask import Flask, redirect, url_for, request, render_template, jsonify
from flask_cors import CORS, cross_origin
import cipher
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
clientLink = "mongodb+srv://test:2cinKpO1locYEb76@cluster1.wjept6s.mongodb.net/?retryWrites=true&w=majority"

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/signup/<username>/<password>', methods=['POST'])
def addNewUser(username, password):
    

    # clientLink = MongoClient("mongodb+srv://test:2cinKpO1locYEb76@cluster1.wjept6s.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)
    client = MongoClient(clientLink, tlsCAfile=ca)
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
    # client = MongoClient("mongodb+srv://test:2cinKpO1locYEb76@cluster1.wjept6s.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)

    client = MongoClient(clientLink, tlsCAfile=ca)
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

@app.route('/createProject/<projectID>', methods=['GET'])
def createProject(projectID):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["Project"]
    col = db["Projects"]
    check = col.find_one({"projectID":projectID})
    if check == None:
        doc = {"projectID":projectID,"HWSet1":0, "HWSet2":0}
        col.insert_one(doc)
        client.close()
        return {"msg": "created project"}
    else:
        client.close()
        return {"msg": "already existing project"}

# @app.route('/deleteProject/<projectID>', methods=['POST'])
# def deleteProject(projectID):
#     client = MongoClient(clientLink, tlsCAfile=ca)
#     db = client["Project"]
#     col = db["Projects"]
#     col.delete_one({"projectID":projectID})
#     dbUser = client["User"]
#     colUser = dbUser["Users"]
#     doc = colUser.find_one({})

@app.route('/getProjectID/<userID>', methods=['GET'])
def getProjectID(userID):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["User"]
    col = db["Users"]
    dicti = col.find_one({"UserID":userID}, {"_id": 0, "Password": 0})
    projID = dicti["ProjectID"]
    return {"projID": projID}

@app.route('/getProjectHW1/<projectID>', methods=['GET'])
def getHW1(projectID):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["Project"]
    col = db["Projects"]
    dicti = col.find_one({"projectID":projectID}, {"_id":0,"HWSet2":0})
    hwSet1 = dicti["HWSet1"]
    client.close()
    return {"hwSet1": int(hwSet1)}

@app.route('/getProjectHW2/<projectID>', methods=['GET'])
def getHW2(projectID):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["Project"]
    col = db["Projects"]
    dicti = col.find_one({"projectID":projectID}, {"_id":0,"HWSet1":0})
    hwSet2 = dicti["HWSet2"]
    client.close()
    return {"hwSet2": int(hwSet2)}

@app.route('/getHWCap/<hwSet>', methods=['GET'])
def getCapacity(hwSet):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["HardwareSet"]
    col = db["Hardware"]
    dicti = col.find_one({"Name":hwSet},{"_id":0})
    capacity = dicti["Capacity"]
    client.close()
    return {"capacity": int(capacity)}

@app.route('/getHWAvail/<hwSet>', methods=['GET'])
def getAvail(hwSet):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["HardwareSet"]
    col = db["Hardware"]
    dicti = col.find_one({"Name":hwSet},{"_id":0})
    avail = dicti["Capacity"]
    client.close()
    return {"availability": int(avail)}

@app.route('/projectCheckIn/<projectID>/<hwSet>/<qty>', methods=['GET'])
def checkIn(projectID, hwSet, qty):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["HardwareSet"]
    col = db["Hardware"]
    dicti = col.find_one({"Name":hwSet}, {"_id":0})
    avail = dicti["Availability"]
    dbProject = client["Project"]
    colProject = dbProject["Projects"]
    dictProject = colProject.find_one({"projectID":projectID},{"_id":0})
    hwSetQty = dictProject[hwSet]
    if qty < 0:
        client.close()
        return {"msg": "error: qty has to be greater than 0"}
    elif hwSetQty < qty:
        client.close()
        return {"msg": "error: qty is bigger than what is checked out"}
    else:
        col.update_one({"Name":hwSet},{"$set": {"Availability":(avail+qty)}})
        colProject.update_one({"projectID":projectID},{"$set": {hwSet:(hwSetQty-qty)}})
        client.close()
        return {"msg": "check in sucessful"}

@app.route('/projectCheckOut/<projectID>/<hwSet>/<qty>', methods=['GET'])
def checkOut(projectID, hwSet, qty):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["HardwareSet"]
    col = db["Hardware"]
    dicti = col.find_one({"Name":hwSet}, {"_id":0})
    avail = dicti["Availability"]
    dbProject = client["Project"]
    colProject = dbProject["Projects"]
    dictProject = colProject.find_one({"projectID":projectID},{"_id":0})
    hwSetQty = dictProject[hwSet]
    if qty < 0:
        client.close()
        return {"msg": "error: qty has to be greater than 0"}
    elif qty > avail:
        client.close()
        return {"msg": "error: requested more qty than available"}
    else:
        col.update_one({"Name":hwSet},{"$set": {"Availability":(avail-qty)}})
        colProject.update_one({"projectID":projectID},{"$set": {hwSet:(hwSetQty+qty)}})
        client.close()
        return {"msg": "check out sucessful"}

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
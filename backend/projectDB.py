from pymongo import MongoClient
import certifi
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

ca = certifi.where()
clientLink = "insert link here"

@app.route('/joinProject/<projectID>', methods=['POST'])
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

@app.route('/getProjectID/<userID>', methods=['POST'])
def getProjectID(userID):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["User"]
    col = db["Users"]
    dicti = col.find_one({"UserID":userID}, {"_id": 0, "Password": 0})
    projID = dicti["ProjectID"]
    return {"projID": projID}

@app.route('/getProjectHW1/<projectID>', methods=['POST'])
def getHW1(projectID):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["Project"]
    col = db["Projects"]
    dicti = col.find_one({"projectID":projectID}, {"_id":0,"HWSet2":0})
    hwSet1 = dicti["HWSet1"]
    client.close()
    return {"hwSet1": int(hwSet1)}

@app.route('/getProjectHW2/<projectID>', methods=['POST'])
def getHW2(projectID):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["Project"]
    col = db["Projects"]
    dicti = col.find_one({"projectID":projectID}, {"_id":0,"HWSet1":0})
    hwSet2 = dicti["HWSet2"]
    client.close()
    return {"hwSet2": int(hwSet2)}

@app.route('/getHWCap/<hwSet>', methods=['POST'])
def getCapacity(hwSet):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["HardwareSet"]
    col = db["Hardware"]
    dicti = col.find_one({"Name":hwSet},{"_id":0})
    capacity = dicti["Capacity"]
    client.close()
    return {"capacity": int(capacity)}

@app.route('/getHWAvail/<hwSet>', methods=['POST'])
def getAvail(hwSet):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["HardwareSet"]
    col = db["Hardware"]
    dicti = col.find_one({"Name":hwSet},{"_id":0})
    avail = dicti["Capacity"]
    client.close()
    return {"availability": int(avail)}

@app.route('/projectCheckIn/<projectID>/<hwSet>/<qty>', methods=['POST'])
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

@app.route('/projectCheckOut/<projectID>/<hwSet>/<qty>', methods=['POST'])
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

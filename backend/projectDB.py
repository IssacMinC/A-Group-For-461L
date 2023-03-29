from pymongo import MongoClient
import certifi
from flask import jsonify
ca = certifi.where()

clientLink = "insert link here"
def createProject(projectID):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["Project"]
    col = db["Projects"]
    check = col.find_one({"projectID":projectID})
    if check == None:
        doc = {"projectID":projectID,"HWSet1":0, "HWSet2":0}
        col.insert_one(doc)
        client.close()
        return "created project"
    else:
        client.close()
        return "already existing project"

# def deleteProject(projectID):
#     client = MongoClient(clientLink, tlsCAfile=ca)
#     db = client["Project"]
#     col = db["Projects"]
#     col.delete_one({"projectID":projectID})
#     dbUser = client["User"]
#     colUser = dbUser["Users"]
#     doc = colUser.find_one({})

def getProjectID(userID):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["User"]
    col = db["Users"]
    dicti = col.find_one({"UserID":userID}, {"_id": 0, "Password": 0})
    projID = dicti["ProjectID"]
    return projID

def getHW1(projectID):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["Project"]
    col = db["Projects"]
    dicti = col.find_one({"projectID":projectID}, {"_id":0,"HWSet2":0})
    hwSet1 = dicti["HWSet1"]
    client.close()
    return int(hwSet1)

def getHW2(projectID):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["Project"]
    col = db["Projects"]
    dicti = col.find_one({"projectID":projectID}, {"_id":0,"HWSet1":0})
    hwSet2 = dicti["HWSet2"]
    client.close()
    return int(hwSet2)

def getCapacity(hwSet):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["HardwareSet"]
    col = db["Hardware"]
    dicti = col.find_one({"Name":hwSet},{"_id":0})
    capacity = dicti["Capacity"]
    client.close()
    return int(capacity)

def getAvail(hwSet):
    client = MongoClient(clientLink, tlsCAfile=ca)
    db = client["HardwareSet"]
    col = db["Hardware"]
    dicti = col.find_one({"Name":hwSet},{"_id":0})
    avail = dicti["Capacity"]
    client.close()
    return int(avail)


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
        return "error: qty has to be greater than 0"
    elif hwSetQty < qty:
        client.close()
        return "error: qty is bigger than what is checked out"
    else:
        col.update_one({"Name":hwSet},{"$set": {"Availability":(avail+qty)}})
        colProject.update_one({"projectID":projectID},{"$set": {hwSet:(hwSetQty-qty)}})
        client.close()
        return "check in sucessful"

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
        return "error: qty has to be greater than 0"
    elif qty > avail:
        client.close()
        return "error: requested more qty than available"
    else:
        col.update_one({"Name":hwSet},{"$set": {"Availability":(avail-qty)}})
        colProject.update_one({"projectID":projectID},{"$set": {hwSet:(hwSetQty+qty)}})
        client.close()
        return "check out sucessful"



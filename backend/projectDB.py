from pymongo import MongoClient
import certifi
from flask import jsonify
ca = certifi.where()

def createProject(projectID, project_name, description, date):
    client = MongoClient("mongodb+srv://rayantejani:abcd@cluster0.quex5af.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)
    db = client["Projects"]
    col = db["Project1"]
    doc = {"Name":project_name,"ID":projectID, "Description":description, "CreationDate":date, "HardWareHistory": ""}
    col.insert_one(doc)
    return

def getProjectName(projectID)
    client = MongoClient("mongodb+srv://rayantejani:abcd@cluster0.quex5af.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)
    db = client["Projects"]
    col = db["Project1"]
    dicti = col.find_one({"ID":projectID}, {"_id":0, "Description":0,"CreationDate":0,"HardWareHistory":0})
    projName = dicti["Name"]
    return str(projName)

def getProjectID(userID):
    client = MongoClient("mongodb+srv://rayantejani:abcd@cluster0.quex5af.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)
    db = client["Users"]
    col = db["users"]
    dicti = col.find_one({"UserID":userID}, {"_id": 0, "Password": 0})
    projID = dicti["Projects"]
    return str(projID)

def getDescription(projectID)
    client = MongoClient("mongodb+srv://rayantejani:abcd@cluster0.quex5af.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)
    db = client["Projects"]
    col = db["Project1"]
    dicti = col.find_one({"ID":projectID}, {"_id":0,"Name":0,"CreationDate":0 ,"HardWareHistory":0})
    desc = dicti["Description"]
    return str(desc)

def getCreationDate(projectID)
    client = MongoClient("mongodb+srv://rayantejani:abcd@cluster0.quex5af.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)
    db = client["Projects"]
    col = db["Project1"]
    dicti = col.find_one({"ID":projectID}, {"_id":0,"Name":0, "Description":0,"HardWareHistory":0})
    createDate = dicti["CreationDate"]
    return str(createDate)


def getHWSets(projectID):
    client = MongoClient("mongodb+srv://rayantejani:abcd@cluster0.quex5af.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)
    db = client["Projects"]
    col = db["Project1"]
    dicti = col.find_one({"ID":projectID}, {"_id":0,"Name":0, "Description":0,"CreationDate":0})
    HW = dicti["HardWareHistory"]
    return str(HW)

def deleteProject(projectID):
    client = MongoClient("mongodb+srv://rayantejani:abcd@cluster0.quex5af.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)
    db = client["Projects"]
    col = db["Project1"]
    col.delete_one({"ID":projectID})

    #Update
    dbUsers = client["Users"]
    colUsers = dbUsers["users"]
    doc = colUsers.find_one({})
    projIDList = doc["Projects"]
    newProjIDList = ""
    str_list = projIDList.split(projectID)
    for element in str_list:
        newProjIDList+=element
    colUsers.update_one({"Projects":projIDList}, { "$set": { "Projects": newProjIDList } })



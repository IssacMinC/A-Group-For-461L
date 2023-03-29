import pymongo

clientLink = "mongodb+srv://test:2123@cluster1.wjept6s.mongodb.net/?retryWrites=true&w=majority"

class projects():

    #Create a new Project object in MongoDB
    def createProject(id):
        client = pymongo.MongoClient(clientLink)
        db = client.Projects
        collection = db.Project1
        proj = {"Name": "",
                "ID": id,
                "Description": ""}
        collection.insert_one(proj)
        client.close

    #Create a new Project object in MongoDB with name and description
    def createProject(name, id, description):
        client = pymongo.MongoClient(clientLink)
        db = client.Projects
        collection = db.Project1
        proj = {"Name": name,
                "ID": id,
                "Description": description}
        collection.insert_one(proj)
        client.close

    #Search for a project based on ID
    def queryProject(id):
        client = pymongo.MongoClient(clientLink)
        db = client.Projects
        collection = db.Project1
        result = collection.find_one({'ID': id})
        client.close
        return result
    
    #Update Project Name
    def createProject(id, name):
        client = pymongo.MongoClient(clientLink)
        db = client.Projects
        collection = db.Project1
        collection.find_one({'ID': id}, {"$set": {'name': name}})
        client.close

    #Update Project Description
    def createProject(id, description):
        client = pymongo.MongoClient(clientLink)
        db = client.Projects
        collection = db.Project1
        collection.find_one({'ID': id}, {"$set": {'description': description}})
        client.close
    
# Test 1: Create a test Project and Search for it
#   projects.createProject("test Name", "test ID", "test Description")
#   print(projects.queryProject("test ID"))
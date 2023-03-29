import pymongo

clientLink = ""

class projects():

    #Create a new Project object in MongoDB based onlyy on id
    def createProject(id):
        client = pymongo.MongoClient(clientLink)
        db = client.Project
        collection = db.Projects
        proj = {"projectID": id,
                "HW1": 0,
                "HW2": 0}
        collection.insert_one(proj)
        client.close

    #Create a new Project object in MongoDB with hardware set info
    def createProject(id, hw1, hw2):
        client = pymongo.MongoClient(clientLink)
        db = client.Project
        collection = db.Projects
        proj = {"projectID": id,
                "HW1": hw1,
                "HW2": hw2}
        collection.insert_one(proj)
        client.close

    #Search for a project based on ID
    def queryProject(id):
        client = pymongo.MongoClient(clientLink)
        db = client.Project
        collection = db.Projects
        result = collection.find_one({'projectID': id})
        client.close
        return result
    
    #Update Project HW Set 1 usage
    def createProject(id, num):
        client = pymongo.MongoClient(clientLink)
        db = client.Project
        collection = db.Projects
        collection.find_one({'projectID': id}, {"$set": {'HW1': num}})
        client.close

    #Update Project HW Set 2 usage
    def createProject(id, num):
        client = pymongo.MongoClient(clientLink)
        db = client.Project
        collection = db.Projects
        collection.find_one({'projectID': id}, {"$set": {'HW2': num}})
        client.close
    
# Test 1: Create a test Project and Search for it
#   projects.createProject("test Name", "test ID", "test Description")
#   print(projects.queryProject("test ID"))
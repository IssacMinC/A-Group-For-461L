import pymongo

clientLink = "mongodb+srv://test:DMfmcal3RyXG9gLl@cluster1.wjept6s.mongodb.net/?retryWrites=true&w=majority"

class projects():

    #Create a new Project object in MongoDB based onlyy on id
    def create(id):
        client = pymongo.MongoClient(clientLink)
        db = client.Project
        collection = db.Projects
        proj = {"projectID": id,
                "HWSet1": 0,
                "HWSet2": 0}
        collection.insert_one(proj)
        client.close

    #Create a new Project object in MongoDB with hardware set info
    def create(id, hw1, hw2):
        client = pymongo.MongoClient(clientLink)
        db = client.Project
        collection = db.Projects
        proj = {"projectID": id,
                "HWSet1": hw1,
                "HWSet2": hw2}
        collection.insert_one(proj)
        client.close

    #Update Project HW Set 1 usage
    def setHW1(id, num):
        client = pymongo.MongoClient(clientLink)
        db = client.Project
        collection = db.Projects
        collection.find_one({'projectID': id}, {"$set": {'HWSet1': num}})
        client.close

    #Update Project HW Set 2 usage
    def setHW2(id, num):
        client = pymongo.MongoClient(clientLink)
        db = client.Project
        collection = db.Projects
        collection.find_one({'projectID': id}, {"$set": {'HWSet2': num}})
        client.close

    #get a project based on ID
    def get(id):
        client = pymongo.MongoClient(clientLink)
        db = client.Project
        collection = db.Projects
        result = collection.find_one({'projectID': id})
        client.close
        return result
    
    #get project HW1 usage based on ID
    def getHW1(id):
        client = pymongo.MongoClient(clientLink)
        db = client.Project
        collection = db.Projects
        result = collection.find_one({'projectID': id})
        client.close
        return result['HWSet1']
    
    #get project HW2 usage based on ID
    def getHW2(id):
        client = pymongo.MongoClient(clientLink)
        db = client.Project
        collection = db.Projects
        result = collection.find_one({'projectID': id})
        client.close
        return result['HWSet2']

    
# Test 1: Create a test Project and Search for it
#   projects.createProject("test Name", "test ID", "test Description")
#   print(projects.queryProject("test ID"))
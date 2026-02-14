
"""

#### Part of: Data_Structure_Algorithm_05

#### Handle: _MUMINUL__ISLAM___

"""

#Actual Code Started Here


#class started
class theHash:
    #Static Method
    @staticmethod
    def hashGenerator(data):
        return (data//100)
# class end  


#Add data to hashmap as key:value
def setHashMap(aHashMap,node):
    while(node!=None):
        data=node.data
        indexID=theHash.hashGenerator(int(data))
        aHashMap.update({indexID:node})
        node=node.nextNode
    print("Hash Set up Successful")

#Search data using hashmap
def searchHashMap(aHashMap,data):
    indexID=theHash.hashGenerator(data)
    if(indexID in aHashMap.keys()):
        return aHashMap.get(indexID) #returning the node which contain given data

#Remove key:value from hashmap
def removeHashMap(aHashMap,node):
    data=node.data
    indexID=theHash.hashGenerator(data)
    aHashMap.hashMap.pop(indexID)



#Status : Complete

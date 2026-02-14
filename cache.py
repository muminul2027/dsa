
"""

#### Part of: Data_Structure_Algorithm_05

#### Handle: _MUMINUL__ISLAM___

"""

#Actual Code Started From Here


from package.subpackage.node import * #bug fixed
from package.subpackage.hash import * #bug fixed

#Class Started
#Least Recently Used Cache Algorithm Applied

class theCache:
    #For Making it simple, assume cache limit 5 item.use node pool
    def __init__(self,aCacheItemList):

        #Instance Properties
        self.node1=theNode(None,None,None)
        self.node2=theNode(None,None,None)
        self.node3=theNode(None,None,None)
        self.node4=theNode(None,None,None)
        self.node5=theNode(None,None,None)


        #Linking Nodes and making LinkedList
        linkingNodes(self.node4, self.node5,         None)
        linkingNodes(self.node3, self.node4,   self.node5)
        linkingNodes(self.node2, self.node3,   self.node4)
        linkingNodes(self.node1, self.node2,   self.node3)
        linkingNodes(None      , self.node1,   self.node2)

        #input data with most 4 digit
        self.node1.data,self.node2.data,self.node3.data,self.node4.data,self.node5.data=aCacheItemList


        #Creating Hash
        self.hashMap={}
        setHashMap(self.hashMap,self.node1)

        print("Cache and Nodes are Created and Running")


    
#Class End


#Put a Value in Cache. if Cache full, del a entry with Least Recently Used Algorithm
def putCache(self,node): #assume implementing node pool. can upgrade capabillty in 2nd update
    pass
   

#Get the Cache. upgrade in 2nd update
def getCache(aCache,data):
    pass
         
#Status: Completed

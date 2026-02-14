
"""

#### Part of: Data_Structure_Algorithm_05

#### Handle: _MUMINUL__ISLAM____

"""

#Actual Code Started From Here

import gc

#class started
class theNode:
    
    #Constructor
    def __init__(self,data,prevNode,NextNode):
        self.data=data
        self.prevNode=prevNode
        self.nextNode=NextNode

#class end


#Traverse Node
def traverseNode(aNode):
    currentNode=aNode
    if(currentNode.nextNode!=None):
        while(currentNode.nextNode!=None):
            currentNode=aNode.nextNode
        return currentNode
    else:
        return None


#Linking Nodes
def linkingNodes(aPrevNode,aNode,aNextNode):
    aNode.preNode=aPrevNode
    aNode.nextNode=aNextNode


#Delete Node
def deleteCurrentNode(aNode):
    prevNode=aNode.prevNode
    nextNode=aNode.nextNode
    #Now delete
    prevNode.nextNode=nextNode
    nextNode.prevNode=prevNode
    #Now clean the memory
    del aNode
    if(gc.isenabled==True):
        try:
            gc.collect(0)
        except:
            return None #gc doesn't matter normally
#Add Nodes

    
        
#Status : Complete
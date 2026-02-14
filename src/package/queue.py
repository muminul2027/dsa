
"""

#### Part of: Data_Structure_Algorithm_05

#### Handle: _MUMINUL__ISLAM___

"""

#Actual Code Started From Here

class theQueue:
    
    #Class Properties

    #Instace Method

    #Constructor
    def __init__(self) -> None:
        self.queue=[]
        self.queueRearIndexCount=0
    
    #Add element
    def enqueue(self,data : int) -> None:
        self.queue.append(data)
        self.queueRearIndexCount+=1
        
    #Remvoe element and Return
    def dequeue(self) -> None | int:
        returnedElement=self.queue[0]
        self.queue.pop(0) #bug fixed
        self.queueRearIndexCount-=1
        return returnedElement
    
    #Return the frist element
    def peek(self) -> int:
        return self.queue[0]
    
    #Check if the queue is empty
    def isEmpty(self) -> bool:
         return True if(self.queueRearIndexCount==-1) else False
    
    #Find the number of element
    def size(self) -> int:
        return self.queueRearIndexCount #small bug available,what if queue is empty

#Status : Complete

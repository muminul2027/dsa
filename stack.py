
"""

#### Part of: Data_Structure_Algorithm_05

#### Handle: _MUMINUL__ISLAM___

"""

#Actual Code Started From Here

class theStack: 

    #Class Properties


    #Instance Method

    #Constructor
    def __init__(self) -> None:
        self.stack=[]
        self.stackItemCount=-1 #bug fixed

    #Add element
    def push(self,data : int) -> None:
        self.stack.append(data)
        self.stackItemCount+=1

    #Remove element and Return
    def pop(self) -> int:
        returnedItem=self.stack[self.stackItemCount]
        self.stack.pop()
        self.stackItemCount-=1
        return returnedItem

    #Return the top element
    def peek(self) -> int | None:
        if self.stackItemCount>=0:
            return self.stack[self.stackItemCount] 
        else:
            return None

    #Check if stack is empty, isEmpty when true==Stack is Empty
    def isEmpty(self) -> bool:
        if self.stackItemCount==0:
            return True
        else:
            return False

    #Find the number of element in stack
    def size(self)->int:
        return ((self.stackItemCount)+1) #bug fixed
    
#Status : Complete
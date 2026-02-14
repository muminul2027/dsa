

########################################################

#PROJECT_NAME: Data_Structure_Algorithm_05

#OWNER/AUTHOR: MUMINUL ISLAM

#HANDLE: _MUMINUL__ISLAM___

#FOLDER: Muminul_Portfolio_Project_Python

#INDEX_FILE: Project_File_Structure.txt

#LICENSE: Proprietary.

#PURPOSE: Evaluation Only [ Job Application ]

#GitHub: https://github.com/muminul2027/dsa

########################################################


#Actual Code Started From Here

from package.stack import theStack
from package.queue import theQueue
from package.cache import *



#Creating a Stack
aStack=theStack()
    #add data
aStack.push(10)
aStack.push(20)
aStack.push(30)
    #print the stack size
print("Your Stack Size is: ",aStack.size())
    #remove data
aStack.pop()
    #print the stack size
print("After Pop Your Stack Size: ",aStack.size())
    #print the stack top
print("Your Stack Top Now: ",aStack.peek())
    #print is stack empty
print("Your Stack Is Empty: ",aStack.isEmpty())
#Stack Is Working




#Creating a Queue
aQueue=theQueue()
    #add data
aQueue.enqueue(40)
aQueue.enqueue(50)
aQueue.enqueue(60)
    #print the queue size
print("Your Queue Size Is: ",aQueue.size())
    #remove data
aQueue.dequeue()
    #print the queue size
print("After Dequeue Your Queue Size Now:", aQueue.size())
    #print the queue front
print("Queue Front Data Is: ",aQueue.peek())
    #print if the queue empty
print("Your Queue Is Empty: ",aQueue.isEmpty())
#Queue Is Working





#Creating a Least Recently Used( LRU ) Cache
    #creating cache data list
aCacheItemList=[1000,2050,3060,4040,5050]
    #creating cache 
aCache=theCache(aCacheItemList)

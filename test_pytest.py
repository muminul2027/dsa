
"""

#### Part of: Data_Structure_Algorithm_05

#### Handle: _MUMINUL__ISLAM___

"""

#Actual Code Started From Here

from src.package.stack import theStack
from src.package.queue import theQueue

def test_initialize_stack():
    test_Stack=theStack()
    test_Stack.push(10)
    assert test_Stack.peek() == 10

def test_initialize_queue():
    test_queue=theQueue()
    test_queue.enqueue(20)
    assert test_queue.peek() ==20


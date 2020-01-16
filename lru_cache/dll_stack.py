import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self, node=None):
        # self.head = node
        # self.tail = node
        # self.length = 1 if node is not None else 0
        self.storage=DoublyLinkedList(None)

    def push(self, value):
        # pass
        self.storage.add_to_tail(value)
      
        
    def pop(self):
        return self.storage.remove_from_tail()
    
        

    def len(self):
        # print(self.storage)
        # print(self.storage.length)
        return self.storage.length


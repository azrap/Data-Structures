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
        # new_node=ListNode(value,None,None)
        # self.length+=1
        # if not self.head and not self.tail:
        #     self.head=new_node
        #     self.tail=new_node
        # else:
        #     new_node.prev=self.tail
        #     self.tail.next=new_node
        #     self.tail=new_node
        

    def pop(self):
        return self.storage.remove_from_tail()
    
        

    def len(self):
        # print(self.storage)
        # print(self.storage.length)
        return self.storage.length


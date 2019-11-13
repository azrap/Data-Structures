from doubly_linked_list import *


class LRUCache:
    """
    Our LRUCache class keeps track of:
    -  the max number of nodes it can hold.
    - the current number of nodes it is holding
    -  a doubly-linked list that holds the key-value entries in the correct
    order
    - as well as a storage dict that provides fast access
    to every node stored in the cache.
    - Least recently used list 
    - once it reaches limit, it deletes the least recently used.
    """

    def __init__(self, limit=10):
        self.limit=limit
        self.dll=DoublyLinkedList()
        self.storage=dict()
        self.size=0


    """
    - Retrieves the value associated with the given key. 
    - Also needs to move the key-value pair to the tail of the order
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # pass
        # print('storage: ', self.storage)
        # print('dll: ', self.dll)
        # # print('HI!')
        if key in self.storage:
            node=self.storage[key]
        
            self.dll.move_to_end(node)
            return node.value[1]
        return None


    """
    Adds the given key-value pair to the cache. 
    The newly-
    added pair should be considered the most-recently used
    entry in the cache. 
    - If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. 
    - Additionally, in the case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #if the limit has been reached:
        if key in self.storage:
            node=self.storage[key]
            self.dll.move_to_end(node)
            return
        
        if self.size == self.limit:
            oldest=self.dll.head.value 
            del self.storage[oldest[0]] #remove the key/value from the dict
            self.dll.remove_from_head() #remove the oldest item from the head
            self.size-=1 #decrease the size by 1
 
        # if key is in the cache, delete the node so you can over
        
        self.storage[key]=value
        self.dll.add_to_tail((key,value))
        print('is there a head value?', self.dll.head.value)
        print('is there a head?', self.dll.head)
        self.size+=1

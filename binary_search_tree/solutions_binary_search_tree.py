import sys

from dll_queue import Queue
from dll_stack import Stack
from doubly_linked_list import *

"""
* Should have the methods `insert`, `contains`, `get_max`.
  
  * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
  * `get_max` returns the maximum value in the binary search tree.
  * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work. 
"""


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

  # Adds the input value to the binary search tree,
  # adhering to the rules of the ordering of elements in a binary search tree.
    # check if there's a new node

    # iterative

    def insert_azra(self, value):
        new_node = BinarySearchTree(value)
        cur_node = self
        while True:
            if value < cur_node.value:
                if not cur_node.left:
                    cur_node.left = new_node
                    return self
                else:
                    cur_node = cur_node.left
            else:
                if not cur_node.right:
                    cur_node.right = new_node
                    return self
                else:
                    cur_node = cur_node.right

    # recursive

    def insert_brian(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert_brian(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert_brian(value)

    def insert(self, value):
        pass

        # Searches the binary tree for the target value and Return True if the tree contains the value
        # False if it does not
        # can stop at the first instance of a value
        # we kno it's not found if we get to a node that doesn't have children
        # when deleting, the smallest child becomes the parent can stop ath teh

    def contains(self, target):
        cur_node = self
        while cur_node.left or cur_node.right:
            if target == cur_node.value:
                return True
            elif target < cur_node.value:
                if not cur_node.left:
                    return False
                else:
                    cur_node = cur_node.left
            else:
                if not cur_node.right:
                    return False
                else:
                    cur_node = cur_node.right
        if cur_node.value == target:
            return True
        else:
            return False

    def recursive_contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        cur_node = self
        while cur_node.right:
            cur_node = cur_node.right
        return cur_node.value

    def recursive_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        cur_node = self
        queue = []
        visited = []
        queue.append(cur_node)
        while len(queue) > 0:
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
            visited.append(cur_node)
            queue.pop(0)
            if len(queue) > 0:
                cur_node = queue[0]
        for a in visited:
            cb(a.value)

    def for_each_recursive(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------\

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # call function on root
    # if left
    #     call on left
    # if right
    #     call on right
    def in_order_print(self, node):

        if node.left:
            node.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # make queue
    # push root into queue
    # while queue not empty
    # if left
    # add left to back
    # if right
    # add right to back

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            cur_node = queue.dequeue()
            print(cur_node.value)
            if cur_node.left:
                queue.enqueue(cur_node.left)
            if cur_node.right:
                queue.enqueue(cur_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # make stack
    # put the root in the stack
    # while stack is not empty
    # Pop the top item in the stack
    # look right
    # push right to the stack
    # look left
    # if there is a left, push to stack

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            cur_node = stack.pop()
            print(cur_node.value)
            if cur_node.left:
                stack.push(cur_node.left)
            if cur_node.right:
                stack.push(cur_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(5)
bst.insert(2)
print(bst.value)

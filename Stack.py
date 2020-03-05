# Sam Cole
# This is the stack class

from LinkedList import LinkedList


class Stack:
    def __init__(self):
        self.myList = LinkedList()

    def push(self, data):
        self.myList.add_to_head(data)

    def pop(self):
        self.myList.remove_end()

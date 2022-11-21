# assignment: PA4 - Calculator
# author: Harshita Bhardwaj
# date: 11/20/22
# file: stack.py is a file that writes the implementation for the Stack ADT. It's intended purpose is to be imported as a module 
    # in another file to utilize the Stack ADT
    # it can also be used to test the implementation in this file
# input: the input to this file directly is the values being used to test if the Stack ADT was implemented properly. 
# output: the out of this file alone is any vals printed as a result of testing
# Note this file is intened to be used in tree.py and calculator.py to help their functions

class Stack:
    def __init__(self):
        # create and empty stack
        self.items = []

    # return if the stack is empty
    def isEmpty(self):
        return self.items == []

    # add an item to top of the stack
    def push(self, item):
        self.items.append(item)

    # remove and return the top item of the stack
    def pop(self):
        return self.items.pop()

    # return the top item from the stack
    # stack is not modified
    def peek(self):
        return self.items[len(self.items)-1]

    # return the size of the stack
    def size(self):
        return len(self.items)
    
# a driver program for class Stack
if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]
    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())
    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
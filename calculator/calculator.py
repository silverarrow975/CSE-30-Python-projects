# assignment: PA 4 - Calculator
# author: Harshita Bhardwaj
# date: 11/18/22
# file: calculator.py is a file that implements a stack and tree in order to calculate the output of 
    # an arithmetic expression entered by the user
    # the file converts the infix expression entered by the user into a postfix expression in order to calculate the result
# input: this file takes an input of an infix arethmetic expression
    # if the user enters "quit" or "q" in place of an expression then the program will terminate
# output: the program will output the result of the arithmetic expression

# import the expression tree
from tree import ExpTree
from stack import Stack # to help convert from 

# convert the infix expression entered by the user to postfix
def infix_to_postfix(infix):
    postfix = ""
    s = Stack()
    for c in infix:
        # if the character is part of the alphabeth or a space add it to the postfix expresion
        if c.isalpha():
            postfix += c + " "
            
        # if an operator is entered 
        # spaces will be ignored
        else:
            pre = get_precedence(c) # get the precedence of the currect operator
            # if the stack if empty just add the operator to the stack
            if s.size() == 0:
                s.push(c)
                
            # otherwise get the precedence of the operator at the top of the stack
            # if the currect operator has lower or equal precedence to the operator at the top of the stack empty the stack
            elif get_precedence(s.peek()) <= pre:
                for _ in range(s.size()):
                    postfix += s.pop()
            # if precedence is greater then add to the stack
            else:
                s.push(c)                    
    

# get the precedence of the operator
def get_precedence(operator):
    # list of valid operators
    validOperators = ["(", ")", "**", "*", "/", "+", "-"]
    
    # only if the character entered a valid operator get its precedence
    if operator in validOperators:
        # assign a precedence val to the operators
        match operator:
            case "(", ")":
                prec = 4
            case "**":
                prec = 3
            case "*", "/":
                prec = 2
            case "+", "-":
                prec = 1
        
        return prec

def calculate(infix):
    pass

# a driver to test calculate module
if __name__ == '__main__':
    print(infix_to_postfix("(5+2)*3"))
    '''
    print("Welcome to Calculator Program!")
    eq = input("Please enter your expression here. To quit enter 'quit' or 'q':")
    
    # while the user doesn't ask to quit keep running the loop
    while(eq != "quit" or eq != "q"):
        # print the calculation
        print(calculate(eq))
        # ask for the infix operation
        eq = input("Please enter your expression here. To quit enter 'quit' or 'q':")
        
    print("Goodbye!")
    
    #######         Tests to make sure the program works        #######
    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
    '''
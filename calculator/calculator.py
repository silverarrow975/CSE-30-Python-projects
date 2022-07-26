# assignment: PA 4 - Calculator
# author: Harshita Bhardwaj
# date: 11/20/22
# file: calculator.py is a file that implements a stack and tree in order to calculate the output of 
    # an arithmetic expression entered by the user
    # the file converts the infix expression entered by the user into a postfix expression in order to calculate the result
# input: this file takes an input of an infix arethmetic expression
    # if the user enters "quit" or "q" in place of an expression then the program will terminate
# output: the program will output the result of the arithmetic expression

# import the expression tree
from tree import ExpTree
from stack import Stack # to help convert from infix to postfix

# convert the infix expression entered by the user to postfix
# is adding an extra space somewhere
def infix_to_postfix(infix):
    postfix = ""
    operators = ["^", "*", "/", "+", "-"] # list of valid operators
    s = Stack()
    
    num = ""
    for c in infix:
        # if c is a digit or a decimal point add it to the number substring
        if c.isnumeric() or c == ".":
            num += c
        # if the character is an opening parentheis automaatically add it to the stack
        # paranthesis always have the highest precedence
        elif c == "(":
            s.push(c)
        # empty out the operator stack
        elif c == ")":
            postfix += num + " "
            num = ""
            postfix += emptyStack(s)
        # if the character is an operator
        elif c in operators:
            # is there is a number stored
            if len(num) > 0:
                # add current nums to postfix
                postfix += num + " "
                # reset num to an empty string
                num = ""
            # if the stack is empty just push the current opperator to the stack
            if s.isEmpty():
                s.push(c)
            else:
                prec = get_precedence(c) # get the precedence of the operator
                # add the operator to the stack if it has higher precedence than the previous operator in the stack
                if prec > get_precedence(s.peek()):
                    s.push(c)
                # if the precedence of the current operator is less than or equal to the operator at the top of the stack 
                # empty the stack into postfix
                # add the current operator to the stack
                else:
                    postfix += emptyStack(s)
                    s.push(c)
                
        # if the character is a space
        else:
            postfix += num + " "
            # reset num to an empty string
            num = ""
            
    # add any remaining number to postfic
    postfix += num + " "
    # empty the stack of operators into postfix
    postfix += emptyStack(s)
            
    return postfix.strip()                   
    
def emptyStack(stack):
    s = ""
    while not stack.isEmpty():
        opp = stack.pop()
        # if the opperator is not a type of parantheis then add it to postfix with a space
        if opp != "(":
            s += opp + " "
        
    return s
# get the precedence of the operator
def get_precedence(operator):
    # list of valid operators
    validOperators = ["^", "*", "/", "+", "-"]
    if operator in validOperators:
        if operator == "^":
            prec = 3
        elif operator == "*" or operator == "/":
            prec = 2
        elif operator == "+" or operator == "-":
            prec = 1
        
        return prec

    return 0 # default return

def calculate(infix):
    postfix = infix_to_postfix(infix) # convert the infix to postfix
    tree = ExpTree.make_tree(postfix.split()) # make an expression tree
    return ExpTree.evaluate(tree) # return the result of the tree

# a driver to test calculate module
if __name__ == '__main__':
    # print(infix_to_postfix("(42+5)*3+7"))
    # print(infix_to_postfix('(5+2)*3') == '5 2 + 3 *')
    # print(infix_to_postfix('5+2*3'))
    
    
    print("Welcome to Calculator Program!")
    eq = input("Please enter your expression here. To quit enter 'quit' or 'q':")
    
    # while the user doesn't ask to quit keep running the loop
    while(eq != "quit" and eq != "q"):
        # print the calculation
        print(calculate(eq))
        # ask for the infix operation
        eq = input("Please enter your expression here. To quit enter 'quit' or 'q':")
        print(eq)
        
    print("Goodbye!")
    
    #######         Tests to make sure the program works        #######
    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
    
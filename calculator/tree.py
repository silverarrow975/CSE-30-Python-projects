# assignment: programming assignment 1
# author: (write your full name here)
# date: (write the date you finished working on the program)
# file: hangman.py is a program that (put the description of the program)
# input: (write input description)
# output: (write output description)

from stack import Stack
class BinaryTree:
    def __init__(self,rootObj=None):
        self.key = rootObj # root val
        self.leftChild = None
        self.rightChild = None
    
    # inserting a left child into the tree
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            
    # insert a right child into the tree
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    # return the right child
    def getRightChild(self):
        return self.rightChild
    
    # return the left child
    def getLeftChild(self):
        return self.leftChild
    
    # set the root val
    def setRootVal(self,obj):
        self.key = obj
    
    # return the root val
    def getRootVal(self):
        return self.key
    
    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s
class ExpTree(BinaryTree):
    # postfix is passed in as in array
    def make_tree(postfix):
        stack = Stack()
        validOperators = ["^", "*", "/", "+", "-"]
        
        for c in postfix:
            # if the chacacter is an operator
            if c in validOperators:
                # make a tree node
                t = ExpTree(c)
                # add left and right trees
                t.rightChild = stack.pop()
                t.leftChild = stack.pop()
                # push the tree to a stack
                stack.push(t)
            # if the character is a number
            else:
                stack.push(ExpTree(c))
        
        return stack.pop()
    
    @staticmethod
    # works
    def preorder(tree):
        s = ''
        if tree != None:
            s = tree.getRootVal()
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
            
        return s
    
    @staticmethod
    # works
    def inorder(tree):
        s = ''
        if tree != None:
            if tree.getLeftChild() != None:
                s += "("
            s += ExpTree.inorder(tree.getLeftChild())
            s += tree.getRootVal()
            if tree.getRightChild() != None:
                s += ExpTree.inorder(tree.getRightChild())
                s += ")"
        return s
      
    @staticmethod
    # works
    def postorder(tree):
        s = ''
        if tree != None:
            s += ExpTree.postorder(tree.getLeftChild())
            s += ExpTree.postorder(tree.getRightChild())
            s +=  tree.getRootVal()
        return s
    
    def evaluate(tree):
        pass
            
    def __str__(self):
        return ExpTree.inorder(self)
   
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert ExpTree.preorder(tree) == '+5*23'
    print(ExpTree.inorder(tree))
    # assert str(tree) == '(5+(2*3))'
    '''
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    # assert ExpTree.evaluate(tree) == 11.0
    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    # assert ExpTree.evaluate(tree) == 21.0
    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f' 
    '''
    # test an ExpTree



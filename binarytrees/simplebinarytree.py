'''
Created on Apr 23, 2023

@author: simonray
'''

from binarytrees.basicbinarytree import BasicBinaryTree
from binarytrees.side import Side
from binarytrees.node import Node


class SimpleBinaryTree(BasicBinaryTree):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BasicBinaryTree, self).__init__(self)
        
    
    def insertRoot(self, value):
        if self._root__:
            raise("root is already defined")
        
        root = Node(value)
        
        return root



    def insertNode(self, value, parent, side):
        if not parent:
            raise("parent is null, can't insert this node")
        
        node = Node(value)
        node.set_parent(parent)
        
        if side == Side.LEFT:
            if parent.get_left():
                node.set_left(parent.get_left())
                node.get_left()._set_parent_node(node)
            parent.set_left(node)
            
        elif side == Side.RIGHT:
            if parent.get_right():
                node.set_right(parent.get_right())
                node.get_right()._set_parent_node(node)
            parent.set_right(node)
            
            
        else:
            raise("side is not set")                
                
        return node, parent
    
    def deleteNode(self, node):
        
        # first check to make sure we can safely delete the node
        if not node.get_parent():
            raise("Node has no parent and is not root")
        
           
        # is node a leaf node?
        if not node.get_left() and not node.get_right():
            self.setParentsChild(node, None)
            
        elif not node.get_right():
            self.setParentsChild(node, node.get_left())
            
        elif not node.get_left():
            self.setParentsChild(node, node.get_right())
            
        else:
            self.removeNodeWithBothChildren(node)

        node.set_parent(None)
        node.set_left(None)
        node.set_right(None)
        
    
    
    def removeNodeWithBothChildren(self, node):
        leftTree = Node(node.get_left())
        rightTree = Node(node.get_right())
        
        self.setParentsChild(node, leftTree)
        
        rightMostChildOfLeftTree = Node(rightTree)        
        while rightMostChildOfLeftTree.get_right():
            rightMostChildOfLeftTree = rightMostChildOfLeftTree.get_right()
            
        rightMostChildOfLeftTree.set_right(rightTree)   
        rightTree.set_parent(rightMostChildOfLeftTree)
        
        
        
        
        
            
    def setParentsChild(self, node, child):
        # if 
        if node == self._root_:
            self._root_ = child
            if child:
                child.set_parent(None)
            return
      

        if node.get_parent().get_left() == node:
            node.get_parent().set_left(child)
        elif node.get_parent().get_right() == node:
            node.get_parent().set_right(child)
            
        else:
            raise("node <" + node.get_data() + "> is neither a left or right child of its parent")
        
        if child:
            child.set_parent(node.get_parent())
            
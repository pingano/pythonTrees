'''
Created on Apr 23, 2023

@author: simonray
'''

from binarytrees.binarytree import BinaryTree
from binarytrees.node import Node

class BasicBinaryTree(BinaryTree):
    '''
    classdocs
    '''
    
    def __init__(self):
        self._root_ = Node()

    def toString(self):
        builder = "";
        builder = builder + self.appendNodeToStringRecursive(self.get_root(), builder)
        return builder.toString()


    def appendNodeToStringRecursive(self, node, builder):
        self.appendNodeToString(node, builder)
        if node.left:
            builder = builder + " L{"
            self.appendNodeToStringRecursive(node.left, builder)
            builder = builder + '}'
        
        if node.right:
            builder.append(" R{")
            self.appendNodeToStringRecursive(node.right, builder)
            builder = builder + '}'

        return builder

    def appendNodeToString(self, node, builder) :
        builder= builder + node.data;
        return builder

        
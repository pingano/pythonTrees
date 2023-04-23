'''
Created on Apr 23, 2023

@author: simonray
'''
import sys


from binarytrees.simplebinarytree import SimpleBinaryTree
from binarytrees.side import Side


def generateSimpleBinaryTree():
    simple_binary_tree = SimpleBinaryTree()
    root = simple_binary_tree.insertRoot(3)
    
    # left sub-tree
    node1, root = simple_binary_tree.insertNode(1, root, Side.LEFT);
    node1.to_string()
    node13 = simple_binary_tree.insertNode(13, node1, Side.LEFT);
    node5 = simple_binary_tree.insertNode(5, node1, Side.RIGHT);
    node6 = simple_binary_tree.insertNode(6, node5, Side.LEFT);

    # Right sub-tree
    node10 = simple_binary_tree.insertNode(10, root, Side.RIGHT);
    node11 = simple_binary_tree.insertNode(11, node10, Side.LEFT);
    node16 = simple_binary_tree.insertNode(16, node10, Side.RIGHT);
    node15 = simple_binary_tree.insertNode(15, node16, Side.LEFT);
    node9 = simple_binary_tree.insertNode(9, node15, Side.LEFT);
    node4 = simple_binary_tree.insertNode(4, node15, Side.RIGHT);
    node2 = simple_binary_tree.insertNode(2, node16, Side.RIGHT);    
    
    
    



def main(argv=None): # IGNORE:C0111

    generateSimpleBinaryTree()


if __name__ == '__main__':

    sys.exit(main())
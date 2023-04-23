'''
Created on Apr 16, 2023

@author: simonray
'''

import os

class Node:

    # also called "value" in a binary tree
    # also called "key" in a binary search tree
    def __init__(self, data=""):  # <-- I added an optional argument here
                                    # see https://www.delftstack.com/howto/python/python-class-optional-arguments/
        self._data_ = data 

        self._left_ = None
        self._right_ = None
        self._parent_ = None  # (used in SimpleBinaryTree + red-black tree)
        
        self._height_ = None  # ( used in AVL trees)
        self._colour_ = None  # ( used in red-black trees)
    

    def getData(self):
        return self._data_
    
    def setData(self, d):
        self._data_ = d

    def PrintTree(self):
        print(self._data_)
        
    def set_parent(self, p):
        self._parent_ = p
        
    def get_parent(self):
        return self._parent_
    
    def set_left(self, p):
        self._left_ = p
        
    def get_left(self):
        return self._left_
    
    def set_right(self, p):
        self._right_ = p
        
    def get_right(self):
        return self._right_    
    
    def set_height(self, p):
        self._height_ = p
        
    def get_height(self):
        return self._height_
            
    def set_colour(self, p):
        self._colour_ = p
        
    def get_colour(self):
        return self._colour_    
    
    def to_string(self):
        summary = "NODE:"
        summary = summary + "<" + str(self.getData()) + ">" + os.linesep
        if self.get_left():
            summary = summary + "--  Left Node [" + str(self.get_left().getData()) + "]" + os.linesep
        else:
            summary = summary + "--  Left Node [" + "unassigned" +  "]" + os.linesep
        summary = summary + "-- Right Node [" + str(self.get_right().getData()) + "]\n"        
        summary = summary + "--Parent Node [" + str(self.get_parent().getData()) + "]\n"
        summary = summary + "--Left Node [" + str(self.get_height) + "]\n"        
        summary = summary + "--Left Node [" + str(self.get_colour) + "]\n"
        
        return summary
        
                
    # A simple test for the class
    def test(self):
        root = Node(10)
        root.PrintTree()
        
        
        
              
    
if __name__ == '__main__':
    Node().test()
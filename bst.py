#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple binary search tree. Works with simple key types numeric or string.
"""

class Node:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

class BinarySearchTree:   
    def __init__(self):
        self.root = None
        
    def get(self, key, node = None):
        if node == None:
            node = self.root
        if key == node.key:
            return node.value
        elif key < node.key:
            if node.left != None:
                return self.get(key, node.left)
        elif key > node.key:
            if node.right != None:
                return self.get(key, node.right)
        else:
            return None
        
    def insert(self, key, value, node = None):
        if node == None: 
            if self.root == None:
                self.root = Node(key, value)
                return
            else:
                node = self.root                
        if key > node.key:
            if node.right == None:
                node.right = Node(key, value)
            else:
                self.insert(key, value, node.right)
        elif key < node.key:
            if node.left == None:
                node.left = Node(key, value)
            else:
                self.insert(key, value, node.left)
        elif key == node.key:
            node.value = value 
        
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A linked list with keys as well as values, essentially an ordered map.
"""

class Node:
    key = None
    value = None
    nextNode = None
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
class LinkedMap:
    head = None
    tail = None
    size = 0
        
    def insertStart(self, key, value):
        node = Node(key, value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.nextNode = self.head
            self.head = node
        self.size = self.size + 1
        
    def insertEnd(self, key, value):
        node = Node(key, value)
        if self.head == None:
            self.head = node
        else:
            self.tail.nextNode = node
        self.tail = node
        self.size = self.size + 1
        
    def insertAt(self, key, value, atNode):
        node = Node(key, value)
        node.nextNode = atNode.nextNode
        atNode.nextNode = node
        self.size = self.size + 1
        
    def getStart(self):
        return self.head.value
    
    def getEnd(self):
        return self.tail.value
    
    def get(self, key):
        node = self.head
        while node != None:
            if node.key == key:
                return node.value
            node = node.nextNode

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple linked list implementation
"""

class Node:
    value = None
    nextNode = None
    def __init__(self, value):
        self.value = value
    
class LinkedList:
    head = None
    tail = None
        
    def insertStart(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.nextNode = self.head
            self.head = node
        
    def insertEnd(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            self.tail.nextNode = node
        self.tail = node
        
    def insertAt(self, value, atNode):
        node = Node(value)
        node.nextNode = atNode.nextNode
        atNode.nextNode = node
        
    def getStart(self):
        return self.head.value
    
    def getEnd(self):
        return self.tail.value

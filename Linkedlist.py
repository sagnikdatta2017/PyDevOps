import os 
import sys 
import re 
import math 


class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
    
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0 
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node       
        
        
        
    def PrintLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        
        
        




print("Enter Number of elements you wish to enter")
var_temp = int(input())
# Create an Object of the class 
var_object = Linkedlist()

for  i in range(0 , var_temp):
    var_element = int(input())
    # Call the  Function defined within the class 
    var_object.append(var_element)

print("The full Linkedlist is as follows")
var_object.PrintLinkedList()


    

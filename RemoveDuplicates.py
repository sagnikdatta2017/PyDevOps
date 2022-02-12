import os 
import re
import math 
import random 

class Duplicate:
    def __init__(self,array):
        self.array = array 
    def DuplicateCalc(self):
        memo = {}
        var_len = len(array)
        result = []
        for i in range (0 , var_len):
            if array[i] in memo:
                memo[array[i]]+=1
            else:
                memo[array[i]] = 1 
        print(memo)
        for  key, val in memo.items():
            if ( val > 1):
                for i in range (0 , var_len-1):
                    if ( i  < len(array)):
                        if ( key ==array[i]):
                            array.remove(key)
                        else:
                            continue
                    else:
                        break
            else:
                continue

        print(array)
        
                
 
        
        
        
print("Enter the element in the array separated by a space")
array = list(map(int,input().split()))
#Create the object 

var_object =  Duplicate(array)
result = var_object.DuplicateCalc()
print(result)

import os 
import  re
import random 
import math


class MinMax:
    def __init__(self,array):
        self.array = array 
    def MinMaxCalc(self):
        print(array)
        result = []
        max1 = self.array[0]
        min1 = self.array[0]
        var_len = len(array)
        for i in range(0 , var_len):
            if (max1  < array[i]):
                max1 = array[i]
        result.append(max1)
        print(array)
        for i in range( 0 , var_len):
            if (min1 > array[i]):
                min1 = array[i]
        result.append(min1)
        return result 
    
            




print("Enter the space separated Values to be put in the array")
array = list(map(int, input().split()))
var_object = MinMax(array)
result = var_object.MinMaxCalc()
print(result)

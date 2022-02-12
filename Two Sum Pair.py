import os 
import re
import math 
import random 

class TwoSum:
    def __init__(self,array, var_sum):
        self.array = array 
        self.var_sumsum = var_sum
    def TwoSumCalc(self):
        memo = {}   # Trying to use the HashMap Method to define the O(n) Time Complexity in such cases 
      
        result = []
        
        for i in range( 0 , len(array)):
            var_target = (var_sum - array[i])
            if var_target in memo:
                result.append(var_target)
                result.append(array[i])
                
            else:
                memo[array[i]] = i 
        result2 = []
        result3 = []
        print(result)
        count = 0 
        count1 = 0 
        for i in range ( 0 , len(result)):
            result2.append(result[i])
            count = count +1 
            if ( count ==  2 ):
                count = 0 
                result3.append(result2)
                result2 = []
            else:
                print("HI")
        print(result3)
        
                
            
      
        
        





print("Enter the Value of the Sum to be found")
var_sum = int(input())
print("Enter Space separated Values of the given array in contiguos memory location")
array = list(map(int, input().split()))
var_object = TwoSum(array,var_sum)
result = var_object.TwoSumCalc()
print(result)


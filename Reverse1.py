class Solution():
    
    def __init__(self , x):
        self.x = x ;
    def reverse(self):

        n = str(abs(x))
        n = n.strip()
        n = n[::-1]
        output = int(n)
        
        # Define the if else statement for the scenario 
        
        if output >= 2**31 -1 and output <= -2**31:
            return 0 
        elif output < 0 :
            return -1 * output
        else :
            return output
     

x = int(input())        
myobject = Solution(x)
res= myobject.reverse()
print(res)


        
        
        
        
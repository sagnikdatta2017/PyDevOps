import os 


class Sort():
    def __init__(self, arr):
        self.arr = arr;
    def Sorted(self):
        length = len(arr);
        for i in range (0 , length):
            for j in range (i+1 , length):
                if (arr[i] > arr[j]):
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        return (arr);

arr = [1,6,3,4,8,12,35,46,78,90]   
myobject = Sort(arr)
res= myobject.Sorted()
print(f"The Sorted array is {arr}")
print(os.getcwd)
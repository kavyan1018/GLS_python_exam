"""
    var_name = {}
    var_namr =  [10, 20, 30, 40, 50]
"""


# arr = [10, 20, 30, 40, 50]
# print(arr)  

# # index 
# print(arr[0])
# print(arr[4])
# print(arr[2])



# user input 

arr = []

n = int(input("Enter the number of elements in the array: "))  # array size

for i in range(n):
    # input element from user
    value = int(input("Enter element : "))
    # values -> array push 
    
    # append -> add the new ele at the end of list 
    arr.append(value)
    
print("Array elements are: ", arr)
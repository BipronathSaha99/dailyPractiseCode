# # Array from user in Python 
# import array
# arr=array.array('i',[])
# n=int(input("Enter the length of array:"))

# for i in range(n):
#     ele=int(input("Enter the next element:"))
#     arr.append(ele)
# print(arr) 

# vals=int(input("Choose the element to find its index:"))
# c=0
# for i in  arr:
#     if i==vals:
#         print("The index number is:",c)
#         break

#     c+=1

# import numpy as np
# arr=np.array([163,345,163,367])
# print(arr)

# import  numpy  as np
# arr=np.array([123,154,546,345,346])
# print(arr[0]+arr[1])
# arr_sum=0
# for i in range(6):
    # arr_sum=arr_sum+arr
# print(arr_sum)

import numpy as np
arr=np.array([[114,115,116,117],[118,119,120,121]])
print(arr)
print(arr[0,1])

print(arr[0,0])
print(arr[0,1])
print(arr[0,2])
print(arr[0,3])

import numpy as np
arr_1=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(arr_1)

print(arr_1[0,0,1]+arr_1[0,0,2]+arr_1[0,0,3])
print(arr_1[1,0,1]+arr_1[1,0,2]+arr_1[1,0,3])


arr_2=np.array([[[120,121,122],[123,124,125]],[[156,155,135],[124,272,182]]])
print(arr_2)

print(arr_1)
print(arr_1.dtype)

arr_3=np.array(['a','d','y'])
print(arr_3.dtype)

#convert data type of a array
arr_4=np.array([12,3.3,5])
print(arr_4.astype(int))
print(arr_4.astype('i'))
print(arr_4.astype(bool))






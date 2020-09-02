# Insertion sort 
#How it works-
'''
step-1:
The first element in the array or list is assumed to be sorted. Take the sec0nd element and st0re it in a key.
Compare the key with the first element. If the first element is greater than key,then key is placed in front of the 
first element .

step-2:
Now the first two elements are sorted.
Take the third element and compare it with the elements on the left of it. Placed it just behind the element smaller than it,then place it at the beginning of the array.

step-3:
Similarly, placed every unsorted element at its correct positon.

'''

#Let's start the Code 
def insertion_sort(nums):

  for index in range(1,len(nums)):

    #assign nums[i] to item 
    item = nums[index]
    #find the position for item variable
    pos=index

    while nums[pos-1]>item and pos>0:
      #place nums[pos] to (pos+1)
      nums[pos] = nums[pos-1]
      pos=pos-1
      
    nums[pos]=item

#input
nums=[9,5,1,3,4]
insertion_sort(nums)
#output
print(nums)

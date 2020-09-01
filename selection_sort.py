#selection sort
def sort(nums):
    #outer loop
    for i in range(5):
        minpos=i
        # inner loop
        for j in range(i,5):
            if nums[j] < nums[minpos]:
        
                minpos=j

        if(minpos!=i):
            # swaping 
            nums[i],nums[minpos]=nums[minpos],nums[i]
#input
nums=[10,5,2,8,7]
sort(nums)
print(nums)

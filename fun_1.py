#------------------------------Function-------------------------------------------------#
# Write a function to print the maximum of the two numbers
'''def max_function(num_1,num_2):
    if num_1>num_2:
        # print("{} is the maximum number".format(num_1))
        return num_1
    else:
        # print("{} is the maximum number".format(num_2))
        return num_2
num_1=int(input("enter first number:"))
num_2=int(input("enter second number:"))
print(max_function(num_1,num_2))'''

#---------------------------Write a function to print the maximum of the three numbers-------------------------#
def max_function(num_1,num_2,num_3):
    if (num_1>num_2 and num_1>num_3):
        # print("{} is the maximum number".format(num_1))
        return num_1
    elif (num_2>num_1 and num_2>num_3):
        # print("{} is the maximum number".format(num_2))
        return num_2
    else:
        return num_3
num_1=int(input("enter first number:"))
num_2=int(input("enter second number:"))
num_3=int(input("enter third number:"))
print(max_function(num_1,num_2,num_3))




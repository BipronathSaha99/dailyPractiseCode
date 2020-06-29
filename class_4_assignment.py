# write a program to determine the largest number among the three numbers.
num_1=input("enter first number:")
num_1=int(num_1)

num_2=input("enter second number:")
num_2=int(num_2)

num_3=input("enter third number:")
num_3=int(num_3)

#-------------------->Conditon<------------------#
if (num_1>num_2  and num_1>num_3):
    print("The largest number is {}".format(num_1))
elif (num_2>num_1 and num_2>num_3):
    print("The largest number is {}".format(num_2))
else:
    print("The largest number is {}".format(num_3))

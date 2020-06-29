# Write a program to determine the smallest number among the four integers.
num_1=int(input('1st number:'))
num_2=int(input('2nd number:'))
num_3=int(input('3rd number:'))
num_4=int(input('4th number:'))

#==================> Condition<======================#
if (num_1<num_2 and num_1<num_3 and num_1<num_4):
    print("{} is the smallest number".format(num_1))

elif (num_2<num_1 and num_2<num_3 and num_2<num_4):
    print("{} is the smallest number".format(num_2))

elif (num_3<num_1 and num_3<num_2 and num_3<num_4):
    print("{} is the smallest number".format(num_3))

else:
    print("{} is the smallest number".format(num_4))    
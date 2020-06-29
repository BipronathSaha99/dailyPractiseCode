# Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
value_1=int(input("enter first number:"))
value_2=int(input("enter last number:"))
for num in range(value_1, value_2+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
#---------------------Example of while loop------------------#
# x=1
# while x<=10:
#     print(str(6)+ 'x' +str(x)+ '='+str(6*x))
#     x=x+1
# n=int(input("enter number:"))
# x=1
# while x<=10:
#     print(str(n)+ 'x'+str(x)+ '='+str(n*x))
#     x=x+1
#-----------------------Number------------------------#
# x=4
# while x<=12:
#     print(x)
#     x=x+1
#---------------------reverse number-------------------------------------#
num=input("enter number:")
num_1=int(num)
sum=0
temp=num_1
while temp!=0:
    rem=temp%10     #keep the modulo of temp in rem
    sum=(sum*10)+rem
    temp=temp//10
print("Reverse number={}".format(sum))
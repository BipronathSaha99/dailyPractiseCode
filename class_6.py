#-------------------------------Condition for Triangle---------------------------------------#
a=int(input("enter first side:"))
b=int(input("enter second side:"))
c=int(input("enter third side:"))

# if ((a+b>c) and (b+c>a) and (c+a>b)):
#     print("valid triangle")
# else:
#     print("invalid triangle")
# using function 
def check(a,b,c):
    if ((a+b>c) and (b+c>a) and (c+a>b)):
            return "valid triangle"
    else:
        return "invalid triangle"

print(check(a,b,c))
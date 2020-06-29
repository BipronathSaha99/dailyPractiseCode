'''
Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 
0 and limit with a label to identify the even and odd numbers. For examaple-
0 even
1 odd
2 even
3 odd
'''
n=int(input("enter the number:"))
def showNumbers(n):
    for i in range(n+1):
        if n%2==0:
            return "even"
        else:
            return "odd"
print(showNumbers(n))
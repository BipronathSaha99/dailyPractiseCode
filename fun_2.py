'''Write a function like fizz_buzz to return a number:
a) if the number is divisible by 3,it should return "Fizz"
b) if it is divisible by 5,it should return "Buzz"
c) if it is divisible by both 3 & 5, it should return  "FizzBuzz"
d) if the number is same then it should return the same number.'''
def fizz_buzz(num):
    if (num%3==0 and num%5==0):
        return "FizzBuzz"
    elif num%3==0:
        return "Fizz"
    elif num%5==0:
        return "Buzz"
    else:
        return num
num=int(input("Enter the number:"))
print(fizz_buzz(num))


'''Write a function called show_stars(rows).If rows is 5. It should print:
*
**
***
****
*****'''
def show_stars(rows):
    
    for i in range(rows+1):
        print("*"*i)
        
rows=int(input("enter rows number:"))
print(show_stars(rows))

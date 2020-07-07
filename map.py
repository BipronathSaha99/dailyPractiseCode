#map

# def myfunc(x):
#     return x+x

# x=[1,2,3,4]
# res=list(map(myfunc,x))
# print(res)

# WE can use lambda expression with map and lambda 
# num=[1,12,2,4]
# x=set(map(lambda a:a+a ,num))
# print(x)

# add two list using map and lambda 

a=['sat','sun','mon','tue']
b=['fri','thr','wed']

add=list(map(lambda a,b:a+b,a,b))
print(list(add))


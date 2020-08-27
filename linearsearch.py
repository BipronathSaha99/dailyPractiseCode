# linear search 
# pos=-1
# #call a find function
# def find(lis,x):
#     #counter
#     i=0
#     #logic
#     while i<len(lis):
#         if lis[i]==x:
#             globals()['pos']=i
#             return True
#         i=i+1
#     return False
# #input
# lis=[12,34,65,9,10,36]
# x=65
# #logic
# if find(lis,x):
#     print("matched at ",pos+1)
# else:
#     print("not matched")

pos=-1
def find(lis,x):
    for i in range(len(lis)):
        if lis[i]==x:
            globals()['pos']=i
            return True
    return False
#input
lis=[12,34,65,9,10,36]
x=9
#logic
if find(lis,x):
    print("matched at",pos+1)
else:
    print("not matched")
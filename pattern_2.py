#1. 
# num=int(input("Enter the rows:"))
# #outer loops to handle rows
# for i in range(num+1):
#     #inner loops to handle columns
#     for j in range(i+1):
#         #print the patern using rows
#         print(i,end=" ")
#     #ends line with rows
#     print("\r")

# # >>---------------------->> function<<---------------------<<
# def  patern(n):
#         # outer loops to handle rows
#     for i in range(n+1):
#         #inner loops to handle columns
#         for j in range(i+1):
#             #print the patern using rows
#             print(i,end=" ")
#         #ends line with rows
#         print("\r")

# n= int(input("Rows number:"))
# patern(n)

#2.
# num=int(input("Enter the rows:"))
# #outer loops to handle rows
# for i in range(1,num+1):
#     #inner loops to handle columns
#     for j in range(1,i+1):
#         #print the patern using rows
#         print(j%i,end=" ")
#     #ends line with rows
#     print("\r")

# >>>----------------function<--------<<<
# num=int(input("Enter the rows:"))
# def patern(n):
#     #outer loops to handle rows
#     for i in range(1,num+1):
#         #inner loops to handle columns
#         for j in range(1,i+1):
#             #print the patern using rows
#             print(j%i,end=" ")
#         #ends line with rows
#         print("\r")
# patern(num)


#3.
# num=int(input("Rows:"))
# k=(2*num)-2
# #outer loops to handle rows
# # start from n
# for i in range(1,num+1):
#     #inner loops to handle columns
#     #values change acc. to outer loops
#     for j in range(1,i+1):
#         print(k,end="")
#         k=k+1
#     # k=k+1
#     #endlines with rows
#     print("\r")

num=int(input("Rows:"))

def pat(num):
    k=(2*num)-2
    #outer loops to handle rows
    # start from n
    for i in range(1,num+1):
        #inner loops to handle columns
        #values change acc. to outer loops
        for j in range(1,i+1):
            # print(k,end="")
            # print(j%k,end="")
            k=k+1
        # k=k+1
        #endlines with rows
        print("\r")

pat(num)


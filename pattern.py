# # Pattern
# n=int(input("Enter value:"))
# for i in range(1,n+1):
#     # print(i,end="")
#     for j in range(1,i+1):
#         print(j%2,end=" ")
#     print()

#    >>------------------>>using function<<---------------------------------<<
# declare a function of pattern 
def pattern(n):
    #outer loops to handle rows
    #start from n
    for i in range(0,n+1):
        #inner loops to handle columns.
        # values change according to outer loops.
        for j in range(1,i+1):
            # print(j%2,end="")
            print("q",end=" ")

        #print lines according to rows
        print("\r")
num=int(input("Enter the value of rows:"))
pattern(num)

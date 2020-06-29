#>>-----------------File---------------------------<<
'''
file=open('oop_9_1.txt','r+')
ele=file.read()
print(ele)
file.write("I\'m waiting for you\n")
file.close()
'''
# with open("oop_9_1.txt") as file:
#     ele=file.read()
#     print(ele)

# try:
#     with open("oop_9_3.txt") as file:
#         ele=file.read()
#         print(ele)
# except Exception as e:
#     print(e)

# print("Hello Bipro")    

# try:
#     with open("oop_9_3.txt") as file:
#         ele=file.read()
#         print(ele)
# except Exception as e:
#     with open("oop_9_err.txt",'w') as log:
#         log.write(str(e))
# print("Hello Bipro")  

# try:
#     file= open("oop_9_1.txt")

# except Exception as e:
#     print("Error",e)
# else:
#     ele=file.read()
#     print(ele)
# finally:
#    file.close()

# with open("oop_9_1.txt",'w') as file:
#     file.write("Math is fun")

# with open("oop_9_1.txt",'a') as file:
#     file.write("Math is fun. Make a fun with polar to cartesian cordinates\n")

# with open("oop_9_1.txt",'a') as new:
#     print("Math is fun. Make a fun with polar to cartesian cordinates\n",file=new)


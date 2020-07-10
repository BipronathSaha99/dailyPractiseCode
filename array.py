import array
vals=array.array('i',[4,5,1,-9])
# # print(vals)
# #for i in vals:
# #    print(i)

# # vals=array.array('f',[4.5,5.5,6.0])

# #Accecing elements
# # print(vals[3])
# # print(vals[2])
# # print(vals[:])
# # print(vals[-1:-2])

# #appending elements
# vals.append(-19)
# print(vals)
# #insert elements
# vals.insert(5,9)
# print(vals)
# #pop
# vals.pop()
# print(vals)
# print(vals.pop(3))
# #index
# print(vals.index(1))
# #upadate
# vals[2]=56
# print(vals)
newarr=array.array(vals.typecode,(a+a for a in vals))
for i in newarr:
    print(i)
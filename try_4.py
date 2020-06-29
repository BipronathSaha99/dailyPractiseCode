# Dictionary
B={'House':'Bipro','bird':'parrot','cat':2,'aircraft':3}
print(B,type(B))
#Accesing the element
print(B['House'])
print(B['bird'])
#Using get() to find the value.
print(B.get('House'))
print(B.get('cat'),type('cat'))
#using get() to find key
print(B.get('v',4))
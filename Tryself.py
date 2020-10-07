'''WRITE A FUNCTION THAT TAKES A LIST OF NAMES AND RETURN THE LONGEST NAME.

EXAMPLE
[JUDE,FELIX,SAM]
RESULT:FELIX'''
'''
#call a function
def names(name_list):
	#take counter
	c=0
	#loop
	for name in (name_list):
		if len(name)>c:
			c=len(name)
			word=name
	return word
#input	
name_list=['jude','felix','sam']
#output
print(names(name_list))
'''
#call function
def names(name_list):
	#empty list
	name_len=[]
	#loop
	for i in name_list:
		name_len.append((len(i),i))
	name_len.sort()	
	return name_len[-1][1]
#inpit	
name_list=['jude','felix','sam']
#output
print(names(name_list))	

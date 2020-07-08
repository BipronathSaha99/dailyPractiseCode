# What is Regular Expression? 
# Regular Expression is tools for manipulating strings
# Why do we need Regular Expression?
# -Varifing that strings match from a pattern
# -Performing substituion string


# Regular Expression is accessed using re module
# using match() 
# import re

# # initalize pattern 
# pattern= r'color'

# if (re.match(pattern,"color")):
#     print("True")
# else:
#     print("False")
# using search() method 
# import re

# # initalize pattern 
# pattern= r'color'
# #initialize string
# string="Red is a color. It is a lovely color"
# if re.search(pattern,string):
#     print("True")
# else:
#     print("False")

# using findall() method 
#using re module
# import re
# # initalize pattern 
# pattern= r'color'
# #initialize string
# string="Red is a color. It is a lovely color"
# print(re.findall(pattern,string))

#again visit with seach() method
# There are some method on search()
# -start()
# -end()
# -span()
import re
#initialize pattern
pattern=r"health"
#initialize string
text="Mental health is very much important more than pysical health"
#logic
keep=(re.search(pattern,text))
#output
if keep:
    print(keep.start())
    print(keep.end())
    print(keep.span())


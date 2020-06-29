'''Write a program :
a) if the citizen's income was not higher than 85,528 thalers, the tax was equal 
   to 18% of the  income minus 556 thalers and 2 cents (this was so called tax relief)
b) if the income was higher than this the amount, the tax was equal to 14,839 thalers 
   and 2 cents, plus 32% of the surplus over 85,528 thalers.'''

'''income=float(input("enter your income:"))
if income<85528 :
    tax=((income*0.18)-(556.02))
    print("Tax={:0.2f}".format(tax))
else:
    tax=(14839.02+(income-85528)*0.32)
    print("Tax={:0.2f}".format(tax))
'''
# using function to solve the problem
def tax_calculator(income):
   if income<85528 :
     tax=((income*0.18)-(556.02))
     return tax
   else:
     tax=(14839.02+(income-85528)*0.32)
     return tax
income=float(input("enter your income:"))
print(tax_calculator(income))


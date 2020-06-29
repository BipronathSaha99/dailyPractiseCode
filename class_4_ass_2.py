result=int(input("What\'s your mark?:")) #take user input values.
#===================>condition for checking grades<=====================#
if (result>=80 and result<=100):
    print("Your grade is: A")
elif (result>=60 and result<=79):
    print("Your grade is: B")
elif (result>=49 and result<=59):
    print("Your grade is: C")
else:
    print("Your grade is F")
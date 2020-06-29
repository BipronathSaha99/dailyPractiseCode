#---------------------------Removing elements-------------------------#
#---we use pop(removes the last member)
#---------remove(removes the given number)--------------------------#
my_list=["earth","mars","aris","makemake","jupiter"]
#--------------------Q_1-----------------------------#
#---------------remove all the elements---------------#
#---------------------'To remove specific elements---------------------------#
my_list.remove("earth")
print(my_list)


#----------------------To clear at a time we use clear()-------------------------#
my_list=["earth","mars","aris","makemake","jupiter"]
my_list.clear()
print(my_list)

#-------------------------To remove only last elements----------------------------#
my_list=["earth","mars","aris","makemake","jupiter"]
my_list.pop(4)
print(my_list)
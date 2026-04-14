# import the datetime module and display the current date:

import datetime
x= datetime.datetime.now()
print (x,"\n")

#return the year and name:a

import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))


"""
 Name : Harish kumar
 Date : 21-july-2024
 Program 1 :a.the  function will create a text file with the current timestamp
            b. Current in the time stamp
 """


#a. importing datetime module 
import datetime 

# datetime.datetime.now() to get 
# current date as filename. 
filename = datetime.datetime.now() 

# create empty file 
def create_file(): 
	# Function creates an empty file 
	# %d - date, %B - month, %Y - Year 
	with open(filename.strftime("%d %B %Y")+".txt", "w") as file: 
		file.write("") 

create_file() 

 
# b.Import date class from datetime module
from datetime import date

# Returns the current local date
today = date.today()
print("Today date is: ", today)




"""
 Name : Harish kumar
 Date : 21-july-2024
 Program 1 :wirte another function to read from a text file.the function will take name of the file and display the content of the file into console
 """




a=str(input("Enter the name of the file with .txt extension:"))
file2=open(a,'r')
line=file2.readline()
while(line!=""):
    print(line)
    line=file2.readline()
file2.close()

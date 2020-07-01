
#Reading

#This shows hows to read a file line by line
#and then the rest of the text
#finally nothing is printed as there is not more text

#file = open("filename.txt", "r")

# print("First Line: " + file.readline())
# print("Second Line: " + file.readline())
# print("Rest of File: " + file.read())
# print("Blank line: " + file.readline())

#file.close()

#-------------------------------------------------------------------

#Reading specific parts

#This will read specific parts of the file using chars
#by calling file.readline() and not printing it we skip a line
#we can use file.seek(0) to go back to the start or
#file.read([number of chars]) will read a certain number of characters

#file = open("filename.txt", "r")

# print("First Line: " + file.readline())
# file.readline())
# print("Third Line: " + file.readline())
# file.seek(0)
# print("Blank line: " + file.readline())
# print("First Line once again: " + file.readline())

#file.close()

#-------------------------------------------------------------------


#Writting

#opens a file called test3 in write mode
# Adds "This is a line" 10 times in, convert in  string
# and the new line function at the end

#file = open("Filename.txt", "w")

#for i in range (1,11):
#    newline = "This is a line " + str(n) + "\n"
#    file.write(newline)

#file.close()


#-------------------------------------------------------------------

#Editing


#write to the file and append to the end of it


#file = open("filename.txt", "r")

#outfile = ""
#for line in range(10):
#    if line % 2 == 0:
#        outfile += file.readline()
#    else:
#        file.readline()

#file = open("filename.txt", "w")
#file.write(outfile)
#file.close()


#-------------------------------------------------------------------





#Create text file
#Enter list of teams
#Enter each team on a new line
#Close text file for writing
#Open text file for reading
#Close text file



file = open("teams2.txt", "w")

teams2 = ["Scotland", "Brazil", "Germany", "France", "England"]

for teams2 in teams2:
    file.writelines(teams2)
    file.writelines('\n')

file.close()


file = open("teams2.txt")
print("First Line: " + file.readline())
file.readline()
file.readline()
print("Fourth Line: " + file.readline())

file.close()


#now need to practice appending it






































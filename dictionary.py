#Μιχαήλ Δανούσης
#321/2012046

import os; 
path=os.path.dirname(os.path.abspath(__file__))
fname="\\dict.txt"


dict ={} #dictionary


#Try to open the file "dict.txt"
#If doesn't exist create a new one
if os.path.isfile(path+fname):
	file= open(path+fname,"r")
	content = file.readlines()
	print("There are ",len(content),"words in the dictionary")
	l=len(content)
	# for every line until eof
	# 	get line, write key until comma and then the value
	for i in range(l):
		line=content[i]
		key=line.split(",",1)[0]
		value= line.split(",",1)[1]
		dict[key]=value
	
	file.close()
else:
	file=open(path+fname,"w")
	print("File created")
	file.close






print("")
print("What do you want to do?")
action = input("('s' for searching a word or 'i' for inserting a new word): ")
if action=='s':
	#search
	key=input("Enter the word you want to search: ")
	if key in dict.keys():
		print("The translation is: ",dict[key])
	else:
		print ("No such word exists")
	
elif action=='i':
	#insert
	newKey=input("Enter the english word you want to insert: ")
	newValue=input("Enter the translation of the word you inserted: ")
	dict[newKey]=newValue
	file= open(path+fname,"a")
	file.write(newKey+","+dict[newKey]+"\n")
	print("The word inserted to the Dictionary")
	file.close()
	

del dict        

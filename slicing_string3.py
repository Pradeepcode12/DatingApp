greeting = "goodmorning"
name = "pradeep"
print(type(name))
#c = greeting + name 
#print (c)
print(name[0:3])
print(greeting[-4:-1])

#STRING FUNCTION

#story = "my name is pradeep prajapati i am currntly doing graduation"
#print(len(story))
#print(story.count("p"))
#print(story.find("pradeep"))
#print(story.replace( "pradeep", "traderpradeep"))

letter = '''Dear <|NAME|>
your are selected 
date: <|DATE|>
'''
print(letter)
name = input("enter your name\n")
date = input("enter date\n")
letter =letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)
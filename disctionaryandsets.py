#distionary 
'''
myDict ={
    "fast":"in a quick manner",
    "pradeep":"A coder",
    "string":(2,4,5) #we can change the value of list in distionary
}
print(myDict["pradeep"])
print(myDict["string"])
myDict["string"]= (4,3,5) #this chane the value of string 

#disctionary method

print(myDict.keys()) #ye disctionary ke keys ko print karega

updateDict={                      #ye disctionary ko update karne ke liye use karenge 

    "lover":'friend',
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("fast"))  #print karega jo fast disctionary elements rhega 
print (myDict["fast"])   # ye abhi yhi print karega jo fast disctionayr me elements rhega 

# the diffrence between .get and [] syntax in dictionary?
print(myDict.get("fast2"))  #return none as fast2 is not present in the distionary
print (myDict["fast2"])   # a throws errors as fast2 is not present in the disctionary 



#SETS

p = {2,1,3,4,6}  #set yesa banate h 
p1={3,4,5,6,7,7,4}  #sets doesnt show repetate value 
print(type(p))
print(type(p1))
print(p)
print(p1)

a ={} # this crete empty disctionary not the empty set 
print(type(a))

b = set()
print(type(b))

#sets method

b = set()
print(type(b))
# adding a vlues in empty sets
#list and distionary  ko sets ke under add nhi kar sakte 
b.add(5)
b.add(4)
b.add(3)
b.add(4)
b.add((1,2,6))
print(b)

print(len(b))  #print the length of sets 

b.remove(5) #remove 5 from set b
#b.remove(12) #throws error not present in the b set  
print(b)

#QUESTION 1
myDict ={
    "waqt":"time",
    "pankha":"fan"

}
print("option are",myDict.keys())
a= input("Enter the hindi word\n")
print("the meaning of your word is :",myDict[a])
'''

#what will be the length of the following set S;

S=set()
S.add(20)
S.add(20.0)
S.add("20")
print(S)









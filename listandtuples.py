# LIST

''' create a list using[]

A = [1, 2, 4, 54, 6]# index no. starts from 0,1,2,3....
print(A[2])  #acess using index using a[0], a[1]

A[3]= 65  #we can change the value from the list 
print(A)

# we can create a list from diffrent types
B = [3, "pradeep",4.3 ]
print(B)


#LIST SLICING
fruits = ["mango", "apple", "grapes", "banana", 34]
print(fruits[0:3])

#LIST Method

L1= [1,43,23,56,54,67,68]
#L1.sort() sort the list 
#L1.reverse()  reverse the list  
#L1.append(69)  ye no.add karega at the end of list
#L1.insert(2,45)  ye index no. ke jagah new no. add karne ke iye use hoga
#L1.pop(3)  ye delete karne ke liye use hota hai
print(L1)


#write a program to store five fruits in a list enterd by the user. 
f1=input("Enter fruit name 1")
f2=input("Enter fruit name 2")
f3=input("Enter fruit name 3")
f4=input("Enter fruit name 4")
f5=input("Enter fruit name 5")
fruitlist=[f1,f2,f3,f4,f5]
print(fruitlist)
print (fruitlist[1:2])

#write a program to sum a list of 5 numbers.

p=[23,13,54,6,78]
p.sort()
print(sum(p))
print(p)
'''



#TUPLES

'''creating a tuple using ()
# cannot change the value of tuple 

t=(2,4,6,5,8)  
#t1=() empty tuple
# t1= (2)ye tuple nhi h 
#t1= (2,) write way to declere tuple 
print(t1)
'''

#TUPLE METHOD

#t=(3,2,1,1,1,1,14,5,6,7,8,9)

#print(t.count(1))  ye count karega ki 1 no, kitne aar aya h 
#print(t.index(3)) ye index no. print karega no. ka 
#print(t.count(3))

#write a program to count the number of zero in the following tuple:
a1=(7,0,4,0,0,9)
print(a1.count(0))
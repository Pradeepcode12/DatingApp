#WHILE LOOP 
'''
i=0
while i<10:
    print("yes" + str(i))
    i = i + 1

    #print("done")

    
fruits =["mango","apple","grapes","watermelon"]
i=0
while i<len(fruits):
        print(fruits[i])
        i= i+1
        
        '''

#FOR LOOP
'''
fruits =["mango","apple","grapes","watermelon"]

for items in fruits:
        Print(items)
'''

'''
# RANGE FUCTION OF PYTHON
for i in range (8):
        print(i)

for i in range (1, 8): #isme 1,8 se iska malab 1 se start hoga or 7 tK jYEGA
        print(i)

'''

'''
#FOR LOOP WITH ELSE 

for i in range(10):
    print(i)

else:
    print("this no. is available in range ")

'''

'''
#BREAK STATEMENT

for i in range(9):
    print(i)
    if i==6:
      break            #ye break karega or 6 tak hi rok dega 


#CONTIUNE STATEMENT 

for i in range(9):
    
    if i==5:
       continue
    print(i)


#PASS STATEMENT

i = 5 
if i > 8:
   pass
print("done")



num = int(input("give the no. for multiplication"))

for i in range(1, 11):
   print(str(num) + "X" + str(i) + "=" + str(i*num))
    # print(f"{num}X{i}={num*i}") ye dusra method h f string 
'''


#write a program to find wheteher a given number is prime or not 

num= int(input("enter the number:"))
prime = True

for i in range(2,num):
   if(num%i == 0):
      prime = False
      break
if prime:
   print("this number is prime")
else:
   print("this is not prime number")


# write a program to calculate the factorial of a given number using for loop

num=int(input("enter the number:"))
factorial = 1
for i in range (1, num+1):
  
   factorial = factorial * i
print(f"the factorial of this number is{factorial}")




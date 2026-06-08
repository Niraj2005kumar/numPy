# outopu , input & operaters 

# output
name = "Niraj"
age = 22
#first option 
print(f"hi I am {name} and my age is {age}")

#second option
print("hi I am {} and my age is {}".format(name,age))

#third option
print("hi I am " + name + " and my age is " + str(age)) #esme age ko string me convert karna padega nahi to error aayega

#fourth option
print("hi  i am ",name," and my age is ",age)




#input
name = input("enter your name :- ")
age = int(input("Enter your age:- ")) # hum apna input ko int me convert kr diye hai or hum yaha bhi kr sakte hai change karne ke liye input ko str me convert kr sakte hai ya float me convert kr sakte hai
#esme user se age input karne ke liye bola jayega aur jo bhi user input karega wo string me store hoga


print(f"your name is :-{name}")
print(f"your age is :- {age}") #esme age ko print karenge to user ke dwara input kiya gaya age print hoga


# Arithematic operators 
#(+ , - , * , / , % , ** , //) eske under aate hai ye sab operators


a = 10
b = 3
c = 5
print (a+b+c)

print(a-b-c)

a = 11
print((a/2))
 


#Floor Division
print(a//2) #esme a ko 2 se divide karenge to 5 print hoga lekin ye floor division hai to ye 5.0 nahi print karega balki 5 print karega  (Floor Division ye hota hai ki jo value point me aane wala rhta hai usko int me hi rkh deta hain)
print(int(a/2)) #humlog esko es traha bhi likh sakte hai


#power operation
print(a**2) #esme a ka power 2 karenge to 121 print hoga


#comparison operators

#(== , != , > , < , >= , <=) eske under aate hai ye sab operators
print(12==12) 
print(12!=12) #12 is not equal to 12 to ye false print karega
print(12>10)    
print(12<10)
print(12>=12)    #12 can be greater than or equal to 12
print(12<=12) #12 can be less than or equal to 12


# logical operators
#(and , or , not) eske under aate hai ye sab operators


#and operator
print(12>10 and 34==34 and 45==45 and 10>20) # agar es condition me kahi ek bhi false hoga to pura condition false print karega

# or operator
print(34==34 or 12==23 or 67==89 or 12==12) # agar es condition me kahi ek bhi true hoga to pura condition true print karega

# not operator
print(not(12==10)) #esme true hai to false print karega or false hai to true print karega


#EXample

print((5>3 and 10 ==10 )or (4!=4 and 2<1))

print((10==10 and 23!=23)or (34 ==12 and bool("hello")))

print(not(5==5 and 3!=4) or (10>20)) 



#assignment operators
#(= , += , -= , *= , /= , %= , **= , //=) eske under aate hai ye sab operators


a = 10  
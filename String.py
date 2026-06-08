
#STRING: String ek data type hai jisme hum text ko store karte hain. String ko hum double quotes (" ") ya single quotes (' ') ke andar likhte hain.

#har ek character (letter ya number ya symbol) unicode hota hai
#Each character in a string is stored with its own Unicode number.

a = "A"
print(ord(a)) 

b = "college" 
print(b[0]) #esme 0 index pe c hai kyu ki string me counting 0 se start hoti hai
print(b[1]) #esme 1 index pe o hai 

#aagar jitna bada index ho to usme bhi ese traha same print karna hoga 

#agar mujhe string ke middle ka koe bhi carecter ko print krna hia to hum uska index number use karenge
# a [start : end : step]
a = "college"
print(a[1:4:5]) #esme 1 index se 4 index tak ke characters print honge
print(a[0:6:5]) #esme 0 index se 7 index tak ke characters print honge lekin step 2 hia to har dusre character ko print karega



# H e l l o    H o w    a r e       y o  u
#  0 1 2 3 4 5  6 7 8 9 10 11 12 13 14 15 16

a = "Hello How are you"
print(a[6:9:1]) #esme 0 index se 3 index tak ke characters print honge
print(a[10:13:1])
print(a[14:17:1])







#TYPE CONVERSION: 
#String ko hum int me convert kar sakte hain agar string me sirf numbers hon to


#INT
a = "123"
b = int(a) #esme string a ko int me convert kar diya
print(b) #esme b ko print karenge to 123 print hoga lekin ye int type ka hoga
print(type(b)) #esme b ka type print karenge to int print hoga


#float

b = float(a) #esme string a ko float me convert kar diya
print(b) #esme b ko print karenge to 123.0 print hoga lekin ye float type ka hoga
print(type(b)) #esme b ka type print karenge to float print hoga

#STRING

a = 123
b = 34.4
c = 12+3j
d = True

a = str(a) 
b = str(b)  
c = str(c) 
d = str(d) 

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

print(d)
print(type(d))



# boolean   
a = 12 
b = 12.4
c = 0
d = ""
e = 0.0
f = True 

print(bool(a)) #esme a ka value 12 hai to ye true print karega
print(bool(b)) #esme b ka value 12.4 hai to ye true print karega
print(bool(c)) #esme c ka value 0 hai to ye false print karega
print(bool(d)) #esme d ka value "" hai to ye false print karega
print(bool(e)) #esme e ka value 0.0 hai to ye false print karega
print(bool(f)) #esme f ka value True hai to ye true print karega


#Explicit Type Conversion (Manually): The conversion of one data type into another by the programmer using functions like int(), float(), str(), etc., is called Explicit Type Conversion (or Type Casting).
# Implicit Type Conversion (Automatically): The automatic conversion of one data type into another by the Python interpreter is called Implicit Type Conversion (or Type Coercion).
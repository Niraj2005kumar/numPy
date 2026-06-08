#Data Type kisi programming language me data ke type ko define karta hai. Yeh batata hai ki variable me kis tarah ka data store hoga.

# types of data types in python
# 1. int (integer) - whole numbers (e.g., 1, 2, 3)
# 2. float (floating-point) - decimal numbers (e.g., 1. 5, 2.5)
# 3. str (string) - sequence of characters (e.g., "hello", "world")
# 4. bool (boolean) - true or false values (e.g., True, False)
# 5. complex (complex numbers) - numbers with a real and imaginary part (e.g., 1 + 2j)
# 6. NoneType - represents the absence of a value (e.g., None)


a = 12
b = 12.5 # <class 'float'>   this ia a p/q form of a number (5/2 = 2.5)
c = -12
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>    
print(type(c)) # <class 'int'>

#COMPLEX NUMBER
d = 1 + 2j   #esko humlog maths me iyota kehte hai
print(type(d)) # <class 'complex'>


# string
name = 'niraj'  #string me hum single quote ya double quote dono ka use kar sakte hai you can any thing store in string
print(type(name))




#boolean  ko hum directly true ya false ke roop me define kar sakte hai
a = True # Always start with capital letter
b = False
print(type(a))
print(type(b))
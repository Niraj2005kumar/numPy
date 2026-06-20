

# Simple Definition (Exam Purpose)

# "Exception Handling ek mechanism hai jo runtime errors ko handle karke program ke normal execution ko continue karne me madad karta hai."


# a = 12
# if a == 12:

# print( "hello")



# ZeroDivisionError

# a = 10 
# b = 0
# print(a/b)


# typeError 
# a = " 10"
# b = 5
# print (a+b)
# esko humlog add nhi kr sakte hia kyu ki ek string or int ko humlog add nhi kr sakte hai 



# a = int(input("please tell your 1st number :- "))
# b = int(input("please tell your 2nd number :-  "))

# try:  # try har ek errors ko catch krta hai  hum ye tab use krte hai jab humlogo ko pata nhi hota hai ki error kab aayega or kaha tab humlog try ka use krte hai 

#     print(a/b)
# except Exception as err:  #try ke sath ek or chis hoti hia ji except hota hai ...try me jo error aata hai usko except ko dedega or o jo bhi error aata hai usko err me save kr leta hai 
#     print("sorry an error occured as {err}")
# else: 
#     print("no errors occured")

# finally: #fillnaly ek esa block hai o har baar chalta hai
#     print ("if there are errors or there are no errors i will run no matter whats ") 



# name = input("tell your number :-")
# print(f"hello your name is {name } ")


# raise

age = int(input("Eter your age :-"))
if age < 18:
    raise TypeError("you RE NO ELIGIABLE")

print("you are elegible")




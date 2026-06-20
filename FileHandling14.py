# Definition

# File Handling ek process hai jisme hum files ko create, open, read, write, append aur close karte hain. Iska use data ko permanently store karne ke liye kiya jata hai.

# Exam Definition

# "File Handling ek mechanism hai jiske through hum files me data ko create, read, write, update aur manage karte hain."


# open("hello.txt","x")       #create a files


# file = open("filehandline14.txt","w")

# data = input("what ypu wants to writes in your file :- ")
# file.write(data)


# for read files ///////////////////


# file = open ("filehandline14.txt","r")

# print(file.read())


# with:- with keyword ka use file ko open karne ke liye kiya jata hai. Iski khas baat ye hai ki file ka kaam khatam hote hi file automatically close ho jati hai, isliye hume close() manually call karne ki zarurat nahi padti.


with open("filehandline14.txt","a") as f:
    f.write("" + " i want to see if it is work or not")
    
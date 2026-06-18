# Dictionary ek mutable (changeable) data type hai jo data ko key-value pairs me store karta hai.

# d = {10:100,20:200,30:300,40:400}

#vanilla python :- eska matlab ye hota hia ki value or key ko direct access kr raha hu 

# d[50] = 500 #create a new key value pair
# print(d[30]) #300 - reading a value 
# d[10] = 100 #update a key value that already exist
# print(d)
#

# methods approach :- 
d = {10:100,20:200,30:300,40:400}

# d.clear()
# print(d)

# q = d.fromkeys([10,20,30,40],50)  # esme sare KEY KI VALUE ME EK HI VALUE HO JATI HIA YAHI KI 50 DIYA HUYA HAI SAB KEY KA VALUE 50 HO JAYEGA  

# print(d.get(10)) #you can directly print the item   matlab ki key ki value ko direct print kr sakte ho 
# print(d.items()) # esme ek list bane ga or ek tupple ke formate me dega output example :- dict_items([(10, 100), (20, 200), (30, 300), (40, 400)])
# print(d.keys())  #esme ki ki value print hoti hai or us key ki output dic ke type me aayega 
# print(d.values())  #esse key ki value print hoti hai 
# print(d.pop(20))   #esme jo pop ke under key likhte hai o pop ho jata hai or us key ki value bhi bahar nikl jati hai or jab hum return dic ko print krte hai to 
                    # key ki value nhi rhti hia example (200
# d.popitem() # esme directly dic ke last element wali key or value ko pop kr deti hai 
print(d.setdefault())                                                        # {10: 100, 30: 300, 40: 400})
print(d)













# class Factory:
#     a = 12 #public class attribute 
#     name = "kia" #public class attribute  /// agar hum name ke aage double under score lagate hia toh hum object me access nhi kr payenge hum ya kuch bhi nhi kr payenge 
#     _old = 12 #AGAR HUM SINGLE UNDERSCORE LAGATE HAI TO YE PROTECTED BAN JATA HIA 
#     def __init__(self , type ,tyre, color):
#         self.type = type # public object attribute        self.tyre = tyre
#         self.__color = color  # private object attribute
#         self.tyre = tyre

#     def detail(self): #public method hai ye 
#         print("hello your details are ")


# class hello(Factory):
#     print(Factory.__name)



# obj = Factory("sedan","MRF","black")

# obj.name = "maruti"

# print(obj.name)



class hello :
    __a = 12

    @classmethod
    def info(cls):
        print(cls.__a)

obj = hello()

obj.info ()      





 

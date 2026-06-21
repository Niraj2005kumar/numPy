from pathlib import Path
import os


def createfile():  # function ko useally uper likha jata hai   
    try:
        name = input("please tell your file name :- ")
        path = Path(name)
        if not path.exists(): # ye line path ko check krne ke liye use kiya ja raha hai
            with open(path,"w") as fs:  # ye line path ko create krne ke liye use kiya ja raha hai 
                data = input("what you want to write:- ")
                fs.write(data)
                print("file create successfully")
        else: 
                print("Error file name already exist")
    except Exception as err:
        print(f"an error occures as {err}")
        

def readfile():

    try:
        name = (input("please tell ypur file name :- "))
        path = Path(name)
        if path.exists():
            with open(path,"r") as fs:
                content = fs.read()
                print(f"your file content is \n {content}")

        else:
            print("error no such file exixts")
    except Exception as err:
        print(f"an error occured as {err}")



def updatefile():

    try:
        name = input("please tell your file name :- ")
        path = Path(name)

        if path.exists():
            print("operation")
            print("1. Renaming the file ")
            print("2. Appending the content")
            print("3. Overwriting the file")
            print ("4. Overwriting the file")

            choice = int(input("Enter your option :- "))

            if choice == 1:
                newname = input("tell your new file name :-")
                new_path = Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("renamed successfully")
                else :
                    print("file already exists")
            elif choice == 2:
                with open(path,'a') as fs:
                    data = input("what do you want to append :- ")
                    fs.write("\n" + data)
                print("successfully append")

            elif choice == 3:
                with open(path,"w") as fs :
                    data = input("what do you want to overwriting :- ")
                    fs.write("\n" + data)
                print("successfully append")
    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:
        name = input("please tell your file name :- ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("file deleted successfully")
        else:
            print("Error no such file exists ")
    except Exception as err:
        print(f"An error occurd as {err}")



print("press 1 for creating a file ")
print("press 2 for read file a file ")
print("press 3 for update a file ")
print("press 4 for delete a file ")


a = int(input("/ntell your response :-")) #/n line ko end krne ke liye use kiye gaya hai 

if a == 1:
    createfile()

if a == 2:
    readfile()

if a == 3:
    updatefile()

if a == 4:
    deletefile()


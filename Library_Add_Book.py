import Library_Dict
import datetime
Datetime=datetime.datetime.now()
Date=Datetime.strftime("Date:%d-%m-%y")
lib_dict=Library_Dict.Library_Dict
def Library_Add_Book():
    for i in lib_dict:
        if i!="Date" and i!="Member":
            user=input(f"Enter The {i}")
            lib_dict[i]=user
        else:
            lib_dict["Date"]=Date
    with open("E:\Python\Library_system.txt","a")as f:
        f.write(str(lib_dict)+"\n")
        print(lib_dict)
        print()
# Library_Add_Book()
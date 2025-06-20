import ast
with open("E:\Python\Library_User_data.txt","r")as f:
    data=f.readlines()
    # print(data)
    # Title=[]
    # datetime=[]
    print(" 一一一一一一一一一")
    print("| User_Name:","user1","|")
    print(" 一一一一一一一一一")
    for i in data:
        user_data=ast.literal_eval(i)
        User_Name=user_data.get("User_Name")
        if User_Name=="user1":
            Title=user_data.get("Title")
            datetime=user_data.get("Date Time")
            print(" 一一一一一一一一一一一一一一一一一一一一一一一一一一")
            print("| Title Of Book:",Title,end=" ")
            print("                         |")
            print("| Date Time:",datetime,end="")
            print("             |")
            print(" 一一一一一一一一一一一一一一一一一一一一一一一一一一")

    # print(" 一一一一一一一一一一一一一一一一一一一一一一一一一一一")
    # print("| Title Of Book:",Title,end=" ")
    # print("|")
    # print(" 一一一一一一一一一一一一一一一一一一一一一一一一一一一")
    # print("Date Time:",datetime)
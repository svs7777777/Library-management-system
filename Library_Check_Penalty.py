import ast
import lb
# import pywhatkit as kit
def Library_Check_Penalty():
    check1={
         "user_name":" ",
         "Check":" "
    }
    with open("E:\Python\Library_User_data.txt", "r") as f:
        data1 = f.readlines()
        check1={}
        for j in data1:
                ans1=ast.literal_eval(j)
                uf=ans1.get("User_Name")
                print(f"Found the book: {uf}")
                check=lb.check(uf)
                print("Penalty",check)
                if check>=0:
                    check1["user_name"]=uf
                    check1["Penalty"]=check
                    with open("E:\Python\check.txt","w")as f:
                        f.write(str(check1))
                    # pri=check
                    # import datetime
                    # datetime=datetime.datetime.now()
                    # th=datetime.hour
                    # tm=datetime.minute
                    # time=th+0
                    # time_mini=tm+1
                    # print(th,tm)
                    # kit.sendwhatmsg(phone, f'{pri}',th,time_mini)
                    # print("Check:",check)
# Library_Check_Penalty()
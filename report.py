import ast
import datetime
class Report:
    def user_report(self):
        with open("E:\Python\check.txt","r")as f:
            data=f.readlines()
            Sum=0
            for i in data:
                ans=ast.literal_eval(i)
                User_Name=ans.get("user_name")
                Penalty=ans.get("Penalty")
                if User_Name=="user9":
                    Sum+=Penalty
            print(User_Name,"Penalty Sum: ",Sum)
    def New_Book_report(self):
        with open("E:\Python\Library_Add_Book.py","r")as f:
            data=f.readlines()
            for i in data:
                ans=ast.literal_eval(i)
                DateTime=ans.get("DateTime")
                print(DateTime)
# U=Report()
# U.user_report()
with open("E:\Python\Library_system.txt","r")as f:
    data=f.readlines()
    for i in data:
        ans=ast.literal_eval(i)
        DateTime=ans.get("DateTime")
        df = datetime.datetime.now()
        total=df.date()
        t=total.strftime("%m")
        d=total.strftime("%d")
        date=datetime.date(2025,3,15)
        dt=date.strftime("%m")
        if dt==t:
            for j in range(1,31):
                
                total=df.date()
                d=total.strftime("%d")
                print(d)
                if j==d:
                    print(ans.get("Title"))
# with open("E:\Python\Library_system.txt","r")as f:
#     data=f.readlines()
#     for i in data:
#         ans=ast.literal_eval(i)
#         DateTime=ans.get("DateTime")
#         print(DateTime)
#         # date=datetime.date(ans)
#         # print(date.strftime("%d"))
#         obj=datetime.datetime.strptime(DateTime, "Date:%d-%m-%y Time:%H:%M:%S")
#         print(obj.strftime("%-d"))
#         # print(obj)
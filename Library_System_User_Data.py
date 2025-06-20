import ast
class Admin:
    def __Admin(self):
        with open("E:\Python\Library_User_data.txt","r")as f:
            data=f.readlines()
            for i in data:
                ans=ast.literal_eval(i)
                print("User Name: ",ans.get("User_Name"))
                print("Title: ",ans.get("Title"))
                print("Issue Date Time: ",ans.get("Date Time"))
                print("Return Date Time: ",ans.get("Return_Date_Time"))
                print("Phone: ",ans.get("Phone"))
                print()

    def Data(self):
        self.__Admin()
Library_System_User_Data=Admin()
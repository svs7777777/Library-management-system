import Admin_Login
import Library_Add_Book
import Library_Book_Search
import Library_Book_Issue
import Library_Return_Book
import Library_Book_Edit
import Library_Book_Delete
import filter1
import Library_System_Data_Show
import Library_System_User_Data

def Admin():
    # User_Name=input("Enter The User Name:")
    # User_Password=input("Enter The Password:")
    User_Name='Admin'
    User_Password='Admin123'
    Login=Admin_Login.Admin_Login(User_Name,User_Password)
    if(Login==2):
        print("  一一一一一一一一一一一一一一一")
        print("| No. |Option                    |")
        print("|  1  |Library_Book_Type         |\n|  2  |Library_add               |\n|  3  |Library_Search            |\n|  4  |Library_Book_Issue        |\n|  5  |Library_Return_Book       |\n|  6  |Library_Book_Edit         |\n|  7  |Library_Delete            |\n|  8  |Library_System_Data       |\n|  9  |Library_System_User_Data  |\n|  10 |Exit")
        print("  一一一一一一一一一一一一一")
        Admin=int(input("Enter the:"))
        print(" 一一一一一一一一一")
        print(f"| Your Selected: {Admin} |")
        print(" 一一一一一一一一一")
        if(Admin==1):
            user=input("Enter The Type Of Book")
            filter1.f.filter(user)
        elif(Admin==2):
                Library_Add_Book.Library_Add_Book()
        elif(Admin==3):
            Ch=input("Enter the Choice:")
            User=input("Enter the Title:")
            Library_Book_Search.Library_Search(Ch,User)
        elif(Admin==4):
            Library_Book_Issue.Library_Book_Issue()
        elif(Admin==5):
            Library_Return_Book.Library_Book_Return() #check the object pass
        elif(Admin==6):
            Library_Book_Edit.Library_Edit()
        elif(Admin==7):
            User_Name=input("Enter The User Name:")
            User_Password=input("Enter The Password:")
            check_condition=Admin_Login.Admin_Login(User_Name,User_Password)
            if(check_condition==2):
                Library_Book_Delete.Library_Delete()
            else:
                print("Not Found")
                exit(0)
        elif(Admin==8):
            Library_System_Data_Show.Library_System_Data.Data()
        elif(Admin==9):
             Library_System_User_Data.Library_System_User_Data.Data()
        elif(Admin==10):
             exit(0)
    else:
            print("Not Found")
            exit(0)
# Admin()
import Library_Book_Search
import Library_Book_Issue
import Library_Return_Book
import filter1
def User_option():
    print("  一一一一一一一一一一一一一")
    print("| No. |Option               |")
    print("|  1  |Library_Book_Type    |\n|  2  |Library_Search       |\n|  3  |Library_Book_Issue   |\n|  4  |Library_Return_Book  |\n|  5  |Exit                 |")
    print("  一一一一一一一一一一一一一")
    us=int(input("Enter The Choice:"))
    print(" 一一一一一一一一一")
    print(f"| Your Selected: {us} |")
    print(" 一一一一一一一一一")
    if(us==1):
        user=input("Enter The Type Of Book")
        filter1.f.filter(user)
    if(us==2):
        Ch=input("Enter the Choice:")
        User=input("Enter the Title:")
        Library_Book_Search.Library_Search(Ch,User)

    elif(us==3):
        Library_Book_Issue.Library_Book_Issue()

    elif(us==4):
        Library_Return_Book.Library_Book_Return()

    elif(us==5):
        exit(0)
# User_option()
import ast
import datetime
def Library_Book_Issue():
    deleted = False
    edit = False
    Title_To_Book = input("Enter the title of the book: ")
    User_Issus_Book=input("Enter The Name:")
    phone_no=input("Enter The Phone_No:")
    updated_books = []
    updated_book = {
        "Title": " ",
        "Author": " ",
        "Member": 0,
        "Date":" ",
        "Phone":" "
    }
    user_issus_book={}

    # Read the existing book data from the file
    with open("E:\Python\Library_system.txt", "r") as f:
        data = f.readlines()
        for i in data:
            ans = ast.literal_eval(i)
            Member=int(ans.get("Member"))
            Title=ans.get("Title")
            if ans.get("Title") == Title_To_Book and Member<=5:
                print("Found the book")
                edit = True
                updated_book["Title"] = ans["Title"]
                updated_book["Author"] = ans["Author"]
                current_member = int(ans.get("Member", 0))
                increment_member= current_member + 1
                updated_book["Member"] = str(increment_member)
                updated_book["DateTime"] = ans["DateTime"]
                updated_books.append(updated_book)


                # User Book Details
                Datetime=datetime.datetime.now()
                dt=Datetime.strftime("%d-%m-%y")
                num='+91'+phone_no
                user_issus_book.update({"User_Name":User_Issus_Book})
                user_issus_book.update({"Title":ans["Title"]})
                user_issus_book.update({"Date":dt})
                user_issus_book.update({"Phone":num})
                user_issus_book.update({"Return_Date_Time":' '})
                with open("E:\Python\Library_User_data.txt", "a") as f:
                    f.write(str(user_issus_book) + "\n")

                deleted = True
            else:
                updated_books.append(ans)
    if deleted:
        with open("E:\Python\Library_system.txt", "w") as f:
            for book in updated_books:
                f.write(str(book) + "\n")

    if edit:
        print(f"Book with title '{Title_To_Book}' has been edited.")
    else:
        print("No book found with that title to edit.")
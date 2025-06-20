import ast
import datetime
import lb
import Library_Check_Penalty
def Library_Book_Return():
    deleted = False
    edit = False
    Title_To_Book = input("Enter the title of the book: ")
    username = input("Enter the Name: ")
    updated_books = []
    updated_book = {
        "Title": " ",
        "Author": " ",
        "Member": 0
    }
    user_issus_book=[]
    user_issus_book1={
        "User_Name":" ",
        "Title": " ",
        "Date":'',
        "Return_Date":' '
    }

    # Read the existing book data from the file
    with open("E:\Python\Library_User_data.txt", "r") as f:
        data1 = f.readlines()
        for j in data1:
            ans1=ast.literal_eval(j)
        # print(ans1.get("Title"))
        # print(ans1.get("User_Name"))
            if ans1.get("Title")==Title_To_Book and ans1.get("User_Name")==username:
                with open("E:\Python\Library_system.txt", "r") as f:
                    data = f.readlines()
                    for i in data:
                            ans = ast.literal_eval(i)
                        # Check if the title matches the one to edit
                            # Member=ans.get("Member")
                            # Title=ans.get("Title")
                            if ans.get("Title") == Title_To_Book:
                                print(f"Found the book: {ans}")  # Print the book found
                                edit = True  # Flag to edit the book
                                # Update the book details if necessary
                                # check=lb.check(username)
                                # print("Check:",check)
                                updated_book["Title"] = ans["Title"]
                                updated_book["Author"] = ans["Author"]
                                # Increment or change the Member status (Assuming Member is an integer)
                                current_member = int(ans.get("Member", 0))
                                updated_book["Member"] = current_member - 1  # Increment the member number
                                updated_book["Date"] = ans["Date"]
                                updated_books.append(updated_book)  # Add updated book to the list
                                deleted = True  # Flag indicating the book has been modified
                            else:
                                updated_books.append(ans)# Keep the unchanged books


                            # User Book Details
                    for k in data1:
                            ans1 = ast.literal_eval(k)
                            if ans1.get("Title")==Title_To_Book and ans1.get("User_Name")==username:

                                user_issus_book1["User_Name"] = ans1["User_Name"]
                                user_issus_book1["Title"] = ans1["Title"]
                                # Increment or change the Member status (Assuming Member is an integer)
                                user_issus_book1["Date"] = ans1["Date"]
                                Datetime=datetime.datetime.now()
                                dt=Datetime.strftime("%d-%m-%y")
                                user_issus_book1["Return_Date"] = dt
                                user_issus_book.append(user_issus_book1)
                                with open("E:\Python\Library_User_data.txt", "w") as f:
                                    for Book in user_issus_book:
                                        f.write(str(Book) + "\n")
                                deleted = True
                                edit=True
                                Library_Check_Penalty.Library_Check_Penalty()
                            else:
                                user_issus_book.append(ans1)  # Keep the unchanged books
    if deleted:
        with open("E:\Python\Library_system.txt", "w") as f:
            for book in updated_books:
                f.write(str(book) + "\n")
    if edit:
        print(f"Book with title '{Title_To_Book}' has been Return.")
    else:
        print("No book found with that title to Return.")
# Library_Book_Return()
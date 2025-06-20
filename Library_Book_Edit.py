import ast
import Library_Dict
lib_dict=Library_Dict.Library_Dict #Library_Dict is a import name
def Library_Edit():
    title_to_delete = input("Enter the title of the book to Edit: ")
    updated_books = []
    updated_book={
    "Title":" ",
    "Author":" ",
    "Member":" ",
}
    # updated_book={}
    # for i in lib_dict.items():
    #     updated_book.update({i})
    deleted = False
    edit=False
    with open("E:\Python\Library_system.txt", "r") as f:
        data = f.readlines()
        for i in data:
            ans = ast.literal_eval(i)
            if ans.get("Title") == title_to_delete:
                for i in updated_book:
                    user=input(f"Enter The {i}")
                    updated_book[i]=user
                    edit = True
            else:
                updated_books.append(ans)
                deleted = True
                
    if deleted:
            with open("E:\Python\Library_system.txt", "w") as f:
                for book in updated_books:
                    f.write(str(book) + "\n")
    if edit:
        with open("E:\Python\Library_system.txt","a")as f:
                f.write(str(updated_book)+"\n")
                print(f"Book with title '{updated_book}' Edited.")

    else:
        print("No book found with that title.")
# Library_Edit("Title")
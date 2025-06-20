import ast
import Library_Dict
Library_Dict=Library_Dict.Library_Dict #Library_Dict is a import name
def Library_Delete():
    title_to_delete = input("Enter the title of the book to delete: ")
    updated_books = []
    deleted = False
    with open("E:\Python\Library_system.txt", "r") as f:
        data = f.readlines()
        for i in data:
            ans = ast.literal_eval(i)
            if ans.get("Title") != title_to_delete:
                updated_books.append(ans)
            else:
                deleted = True
    if deleted:
            with open("E:\Python\Library_system.txt", "w") as f:
                for book in updated_books:
                    f.write(str(book) + "\n")
            print(f"Book with title '{title_to_delete}' deleted.")
    else:
        print("No book found with that title.")
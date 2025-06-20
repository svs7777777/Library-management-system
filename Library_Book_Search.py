import ast
import Library_Dict
Library_Dict=Library_Dict.Library_Dict
def Library_Search(choice,user):


    with open("E:\Python\Library_system.txt","r")as f:
        data=f.readlines()
        for i in data:
            ans=ast.literal_eval(i)

            title=ans.get("Title")
            author=ans.get("Author")
            member=ans.get("Member")
            # print(title,"\n")
            if(choice=="Title"):
                    if(title==user):
                        if(member<=5):
                            print(f"\nTitle:{title}")
                            print(f"Author:{author}")
                            print(f"Member:{member}\n")
                            break
                        else:
                            print("Book Is Not")
            elif(choice=="Author"):
                    if(author==user):
                        if(member<=5):
                            print("\nTitle:",title)
                            print("Author:",author)
                            print("Member:",member)
                            break
                    else:
                        print("Not found")
            else:
                print("Valid Choice")
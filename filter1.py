import ast
class filter:
    def filter(self,user):
        with open("E:\Python\Library_system.txt","r")as f:
            data=f.readlines()
            print("  一一一一一一一一一一一一一一一一")
            print("|\tTitle\t\t| Author")
            print("  一一一一一一一一一一一|一一一一")
            for i in data:
                ans=ast.literal_eval(i)
                type1=ans.get("Type")
                if type1==user:
                    print("|",ans.get("Title"),"\t|",end=" ")
                    print(ans.get("Author"))
            print("  一一一一一一一一一一一一一一一一")
f=filter()
import ast
import datetime
# User_Name=input("Enter The Name:")
def check(uf):
    with open("E:/Python/Library_User_data.txt", "r") as f:
        data = f.readlines()
        for i in data:
            ans = ast.literal_eval(i)
            if ans.get("User_Name")==uf:
                dt = ans.get("Date")
                t = datetime.datetime.strptime(dt,"%d-%m-%y")
                df = datetime.datetime.now()
                # Calculating time difference
                dtf = df - t
                # Printing the difference
                # print(f"Time difference: {dtf.days}")
                count=0
                if dtf.days>=14:
                    for i in range(0,dtf.days):
                        count=count+5
        return count
Login_Dict={
    "User_Name":"Admin",
    "Password":"Admin123"
}

def Admin_Login(User_name,User_password):
    check=0
    user_name=User_name
    user_password=User_password

    User_input_login={
        "User_Name":" ",
        "Password":" "
    }

    User_input_login.update({"User_Name":user_name})
    User_input_login.update({"Password":user_password})
    for i in Login_Dict.values():
        # print(i)
        for j in User_input_login.values():
            # print(j)
            if(i==j):
                check+=1
    return check
# User_Name="Admin"
# User_Password="Admin@123"
# n=Admin_Login(User_Name,User_Password)
# print(n)
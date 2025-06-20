import Admin as Ad
import User_option as Us
Choice=int(input("1.Admin Login\n2.User Login\nEnter The No."))
if Choice==1:
    Ad.Admin()
elif Choice==2:
    Us.User_option()
else:
    print("Enter The Valid Choice")
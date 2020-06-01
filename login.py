print ("\n")
username = input("Enter The Username: ")
password = str (input("Enter The Password: "))
count = 3  #num of trys
while username != "admin" or password != "123":
    count -=1 
    if count == 0:
        print ("\n you try many time wrong try again later .\n")
        exit()
    else:    
        print("\nwrong password or username , try again \n")
        print("you have a " +str (count)+ " of trys \n")
        username = input("Enter The Username: ")
        password = input("Enter The Password: ")
while username == "admin" and password == "123":
        
    print ("\n welcome to your program \n")
    exit()
#username = admin
#password = 123
#|===================|
#| coder : ahmadNer  |
#|===================|

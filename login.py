username = input("Enter The Username: ")
password = str (input("Enter The Password: "))
count = 3  #for just 3 trys
while username != "admin" and password != "123":
    count -=1 
    if count == 0:
        print ("\n you try many time wrong try again later .\n")
        exit()
    else:    
        print("\n wrong password or username , try again \n")
        username = input("Enter The Username: ")
        password = input("Enter The Password: ")
while username == "admin" and password == "123":
        
    print ("\n welcome to your program \n")
    exit()

from unicodedata import name

granted = False
def grant():
    global granted
    granted = True
def Login (name, password):
    sucess = False
    file = open("user and pass.txt", "r")
    for i in file:
        a,b = i.split(",")
        b=b.strip()
        if(a==name and b==password):
            success=True
            break
        file.close()
        if (success):
            print("Login Successful")
            grant()
        else:
            print("Wrong username or password")
            
def register(name, password):
    file = open("user and pass.txt", "a")
    file.write("\n"+name+","+password)
    file.close()
    grant()

def access(option):
    global name 
    if (option == "Login"):
        name = input ("Enter your name: ")
        password = input("Enter your password: ")
        Login(name, password)
    else:
        print("Enter your name and password: ")
        name = input ("Enter your name: ")
        password = input("Enter your password: ")
        register(name, password)

def begin():
    global option
    print("Welcome to Sewa")
    option = input("Login or Register (Login, reg): ")
    if (option !="Login" and option != "reg"):
        begin()
begin()
access(option)

if (granted):
    print("Welcome to Sewa")
    print("Username: ", name)



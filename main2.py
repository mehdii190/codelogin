users={}
while(True):
    choice=input("what is your plan: ")
    if (choice=="submit"):
        user=input("enter your user: ")
        password=input("enter your password: ")
        cpass=input("enter your pass again: ")
        if(user in users):
            print("username already exist")
        elif(len(password)<8):
            print("password length error!")
        elif(password!=cpass):
            print("pass confirm error!")
        else:
            users[user]=password
            print("submit done!")
            #test
            #print(users)
    elif(choice=="login"):
        user=input("user: ")
        password=input("password: ")
        if((user in users)and users[user]==password):
            print("welcome to your account!")
        else:
            print("user or pass is wrong!")
    elif(choice=="delete"):
        user=input("user: ")
        password=input("pass: ")
        if((user in users) and users[user]==password):
            confirm=input("are you sure?[yes/no]")
            if(confirm=="yes"):
                users.pop(user)
                print("account deleted!!")
            else:
                print("operation canceled!")
        else:
            print("wrong user or pass!!")
    elif(choice=="exit"):
        break
    else:
        pass

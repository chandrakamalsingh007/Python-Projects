email = input("Enter your email :")#g@g.in
k,j=0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper(): # w-- W==w
                            j=1
                    elif i.isdigit():
                                
                if k==1 or j==1:
                    print("Wrong Email 5th condition")
            else:
                print("Wrong Email 4th condition.")
        else:
            print("Wrong Email 3rd condition.")
    else:
        print("Wrong Email 2nd condition.")
else:
    print("Wrong Email 1st condition.")

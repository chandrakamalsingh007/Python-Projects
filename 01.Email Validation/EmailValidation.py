email = input("Enter your email :")#g@g.in

if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@") == 1):
            pass
        else:
            print("Wrong Email 3rd condition.")
    else:
        print("Wrong Email 2nd condition.")
else:
    print("Wrong Email 1st condition.")

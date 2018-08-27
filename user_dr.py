from User import User
from uuid import uuid4
import hashlib



if __name__ == "__main__":

    username = str(raw_input("Enter username: "))
    count = 3

    while(count >= 1):
        passwd = str(raw_input("Enter password: "))
        passwd_again = str(raw_input("Confirm password: "))

        if(passwd == passwd_again):
            pass_hash = hashlib.sha256(passwd).hexdigest()
            
            a = User(name=username,uid=str(uuid4()), passwd=str(pass_hash))
            a.save()
            count = -5
        else:
            print("Passwords do not match.")
            count -= 1


    if(count != -5):
        print("Bad passwords after 3 attempts. Exiting.")
    else:

        test_user = str(raw_input("Enter Username- "))

        b = User.objects.filter(name=test_user)[0]

        test_passwd=hashlib.sha256(str(raw_input("Enter Password- ")))

        if(test_passwd.hexdigest() == str(b.passwd)):
            print("Welcome back {} !".format(test_user))
        else:
            print("Fuck off {}! Seriously what were you thinking!?!".format(test_user))

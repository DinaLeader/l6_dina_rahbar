def check_password(password) :
    '''
    check kardan-e password
    '''
    if len(password) > 8 :  
        if not password.isdigit() or not password.isalpha() :
            if not password.islower() or not password.isupper() :
                print('password sabt shod.')
            return password
    else :
        print('password kamel nist.')

pw = check_password('eghfuwh') #password kamel nist
pw = check_password('egWEF36732') #password sabt shod.




#b
def check_password(password) :
    '''
    check kardan-e password ba T/F
    '''
    if len(password) > 8 :  
        if not password.isdigit() or not password.isalpha() :
            if not password.islower() or not password.isupper() :
                print('True')
            return password
    else :
        print('False')




#c
def check_password_strength (password) :
    '''
    check kardan-e ghodrat-e password va nomre dehi
    '''
    if len(password) >= 8 :  
        if not password.isdigit() or not password.isalpha() :
            if not password.islower() or not password.isupper() :
                print('emtiaz-e 4')

    elif len(password) >= 8 :  
        if not password.isdigit() or not password.isalpha() :
            print('emtiaz-e 3')

    elif len(password) >= 8 :  
        print('emtiaz-e 2')

    elif len(password) < 8 :
        print('emtiaz-e 1')





myP = check_password_strength('hwiwGW') #emtiaz-e 1
myP = check_password_strength('hwiwGW46357') #emtiaz-e 4




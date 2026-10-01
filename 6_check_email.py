def check_email(email) :
    '''
    aya email motabar ast ya na? T/F
    '''
    shart1 = '@' in email
    shart2 =' ' not in email 
    shart3 ='.com' in email
    all_shart = [shart1,shart2,shart3]
    if all(all_shart) :
        print('True')
        return True
    else :
        print('False')
        return False
myemail = check_email('dinaleader@gmail.com') #True
myemail = check_email('dina ledaer.gmail') #False


def name_cleaner(name , lastname) :
    '''
    nam va nem-e khanevadegi-e vared shode
    ra moratab mikonad
    '''
    name = name.title().strip()
    lastname = lastname.title().strip()
    clean = name + ' ' + lastname
    print(clean)
    return clean


me = name_cleaner(' diNa  ' , 'rahbar' ) #Dina Rahbar



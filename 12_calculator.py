def calculator(numb1, numb2, operation):
    '''
    mashin hesab-i shamel-e amaliat-e zarb , taghsim
    va jam-o tafrigh
    '''
    if operation == 'jam':
        numb3 = numb1 + numb2
    elif operation == 'menha':
        numb3 = numb1 - numb2
    elif operation == 'taghsim':
        numb3 = numb1 / numb2
    elif operation == 'zarb':
        numb3 = numb1 * numb2
    else:
        return None

    print(numb3)
    return numb3

calculator(20, 10, 'zarb') #200



























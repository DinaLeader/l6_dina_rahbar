def count_letter(word , letter) :
    '''
    shomaresh-e horoofe moshakhas shode dar 
    kalame dade shode
    '''
    count = 0
    for char in word :
        if letter == char :
            count += 1
    print(count)
    return count

word = count_letter('diana', 'a') #2




#b
def count_letter(word , letter) :
    '''
    shomaresh-e horoofe moshakhas shode dar 
    kalame dade shode
    '''
    return word.count(letter)

count_letter('banana', 'a') #3














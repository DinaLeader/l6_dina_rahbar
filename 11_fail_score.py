def faild_score(scores : list) :
    '''
    nomre haye pass shode ro az fail joda mikoone.
    '''
    pass_scores = []
    for number in scores :
        if number >= 10 :
            pass_scores.append(number)
    print(pass_scores)
    return pass_scores

faild_score([10,20,18,15,6,19,7]) #[10, 20, 18, 15, 19]





#b
def faild_score(scores : list) :
    '''
    nomre haye fail ro az pass joda mikoone.
    '''
    fail_scores = []
    for number in scores :
        if number < 10 :
            fail_scores.append(number)
    print(fail_scores)
    return fail_scores

faild_score([10,20,18,15,6,19,7]) #[6, 7]





#c
def faild_score(scores : list) :
    '''
    tedade afradi ke pass shodan ro barmogardoone.
    '''
    pass_scores = []
    for number in scores :
        if number >= 10 :
            pass_scores.append(number)
    print(pass_scores)
    return len(pass_scores)

faild_score([10,20,18,15,6,19,7]) #3

def rational_decision(info, person):
    table = info[person]
    choice_if_other_not_confess = 0 if table[0][0] <= table[1][0] else 1
    choice_if_other_confess = 0 if table[0][1] <= table[1][1] else 1

    if choice_if_other_not_confess == choice_if_other_confess:
        return choice_if_other_not_confess  # 0 = not confess, 1 = confess
    else:
        return None
    
# choices = ['not confess', 'confess']
# s = {'Lobha': [[3, 10], [1, 5]], 'Raga': [[3, 10], [1, 5]]}
# p = 'Lobha'
# r = rational_decision(s, p)
# print(p, ':', choices[r])
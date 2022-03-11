def win_money(lottery_list):
    import random
    import collections
    random_list = []
    x = (random.randint(0, 9))
    i = 1
    while i < 2:
        random_list.append(x)
        i += 1
    print("Winning Numbers:",lottery_list)  
    print("My Random Numbers:",random_list)
    if collections.Counter(random_list) == collections.Counter(lottery_list):
        return(print("Congrats on winning $1,000,000!!!"))
    else:
        return(print("Aww...try again next time"))

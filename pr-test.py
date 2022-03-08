def my_fun(char1, char2, input_string):
    char1_occur = input_string.count(char1)
    char2_occur = input_string.count(char2)
    if char1_occur == char2_occur:
        print(True)
    else:
        print(False)
        
my_fun('o', 'y', 'Jolly')
my_fun('J', 'l', 'Jolly')

#Count the number of vowels in a string
def vowels_num(x):
    list = ['a', 'e', 'i', 'o', 'u']
    n = 0
    for i in x:
        if i in list:
            n+=1
    return n


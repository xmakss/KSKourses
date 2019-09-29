def evklid(a, b):
    if(a > b):
        while(b % a != 0):
            c = a
            a = b
            b = c % a
        return print(a)
    else:
        while (a % b != 0):
            c = b
            b = a
            a = c % b
        return print(b)
evklid(106,16)
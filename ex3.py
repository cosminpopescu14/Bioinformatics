import  string

##adn = 'ACTG'
##a = 'ACTG'
##b = 'TGAC'
##
##x = adn.maketrans(a, b)
##print(adn.translate(x)[::-1])

def catenaADN(adn):   
    a = 'ACTG'
    b = 'TGAC'

    x = adn.maketrans(a, b)
    return adn.translate(x)[::-1]

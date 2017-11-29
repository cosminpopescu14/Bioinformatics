#exercitiul 1 punctul c
import  string

def catenaADN(adn):   
    a = 'ACTG'
    b = 'UGAC'

    x = adn.maketrans(a, b)
    y = adn.translate(x)[::]
    
    return y


print(catenaADN("ATCGAACAATCAAGC"))



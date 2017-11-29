#exercitiul 1 punctele a si b
from random import *
from test.pickletester import MyList


def adn(n):
    adn = ['a', 'c', 't', 'g']
    return ''. join(random.choice(adn) for x in range(n))



def adn1(n):
    a={0:"A",1:"T",2:"G",3:"C"}
    
    mylst = []
    
    for i in range(n):
        mylst.append((a[randint(0,3)],a[randint(0,3)],a[randint(0,3)]))
    print(mylst)
    return(mylst)

x = adn1(5)
print(x)
def afisare(x):
    
    s = ''
    for i in x:
       
       s = s + i[0] + i[1] + i[2]
       
    print(s)
    return s
       

print(afisare(x))
    
    
    




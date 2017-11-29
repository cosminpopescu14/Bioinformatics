sir = "Ana a castigat concursul international de sah de la Kutna Hora"

sir_split = sir.split(' ')
lista_cuv = []
for i in  range(0, len(sir_split)):
    
    if len(sir_split[i]) <= 3:
        sir0 = lista_cuv.append(sir_split[i])

    elif len(sir_split[i]) == 4:
        sir1 = sir_split[i][1 : 3]
        lista_cuv.append(sir1)

    else:
        
        c = sir_split[i]
        lastChar = len(c)
        sir2 = c[0 : 2]
        sir3 = c[lastChar - 2 : lastChar]

        sir4 = sir2 + sir3


print(lista_cuv, sir4)



 

    


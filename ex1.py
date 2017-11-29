sir = "Rezultatele lui Sebastian in seiunea tocmai incheiata sunt: IRA={nota_IRA}, SCPI={0}, MPB={2}, PS={nota_PS}, IB={1}"
sir = sir.format('4','10','8',nota_IRA='4',nota_PS='6')
print(sir)

def ex1(sir,nota):
    siruri = sir.split(' ')
    sirNou = ''
    for i in range(0, len(siruri) ):
        index = siruri[i].find(str(nota)) 
        if index < 0:
            sirNou = sirNou + siruri[i] + ' '
    return sirNou

sir2 = ex1(sir,'1')
sir3 = ex1(sir,'2')
sir4 = ex1(sir,'3')
sirFinal = ex1(sir,'4')

print(sirFinal)


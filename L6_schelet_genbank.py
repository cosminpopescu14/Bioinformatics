import string

def extractDNA(fin, fout):
    # TODO: de extras adn (de la 'ORIGIN' pana la '//') si de scris  in format fasta
    file = open(fin, 'r')
    out_file = open(fout, 'w')

    for line in file:
        if line.strip() == 'ORIGIN':
            break
        

    for line in file:
        if line.strip() == '//':
            break

        sir = line[10:].replace(' ', '')
        out_file.write(sir.upper())
    file.close()
    out_file.close()


def compl(str): 
    # intoarce secventa de adn complementara lui str
    # TODO: de testat
    tb = str.maketrans('ATCG', 'TAGC') # tabela de translatie
    return str.translate(tb)[::-1] # face traslatarea efectiva si inversarea secv

def complement(str,fADN):
    #trateaza complement
    
    #sari dupa sirul "complement (" si elimina ultima ")"
    str = str[len('complement('):-1] 
    
    if str[0] in '123456789':
        # extragere capete
        index = str.find('.')
        a = int(str[:index]) - 1
        b = int(str[index+2:]) - 1
        return compl(extractGeneFromFile(a,b,fADN))
    elif str[0] == 'j':
        return compl(join(str,fADN))
    
    return False
    
def join(linie, fADN):
    #trateaza join
    # TODO: elimina cuvantul "join(" si ultima ")"
    # TODO: concatenarea secventelopen()or genei
    # HINT: folositi functiile split si strip

    str_array = linie[5 : len(linie) - 1].split(',')
    string = ''

    for elem in str_array:

        index = elem.find('..')
        a = int(elem[: index]) - 1
        b = int(elem[index + 2 :])

        string += extractGeneFromFile(a,b,fADN)
        print(string)

    return string
    pass

def extractGeneFromFile(a,b,fADN):
    # TODO: de extras o gena de la pozitia a la b din fisierul fADN (sequences.adn)
    #sunt 60 de caractere pe fiecare linie, pe ultima linie pot fi mai putine
    #se trece peste prima linie - vezi format fasta
    fisier = open(fADN, 'r')
    fisier.readline()
    sir = fisier.read().replace("\n", "")[a : b]
    fisier.close
    return sir
 

def extractGene(str, fADN):
    str = str.strip()
    str = str.replace('<', '')
    str = str.replace('>', '')
    
    if str[0] in '123456789':
        # extragere capete
        index = str.find('.')
        a = int(str[:index]) - 1
        b = int(str[index+2:]) - 1
        return extractGeneFromFile(a,b,fADN)
    
    elif str[0] == 'c':
        return complement(str, fADN)
    elif str[0] == 'j':
        return join(str, fADN)
    
    return False

def readGenes(fgenbank, fADN, fout):
    f = open(fgenbank,'r')
    g = open(fout,'w')
    
    data = f.readline()
    while 'ORIGIN' not in data:
        if data[5:9] == 'gene':
            g.write(extractGene(data[21:], fADN) + '\n')
        data = f.readline()
    g.close()
    f.close()
    
if __name__ == '__main__':
    extractDNA('sequence.gb', 'sequence.adn')
    readGenes('sequence.gb', 'sequence.adn', 'sequence.genes')

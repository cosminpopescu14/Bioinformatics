#ex3c lab6
def readProteicSeq(SecvProteica):

    
    fisier = open(SecvProteica, 'r')
    next(fisier)

    for line in fisier:
        linieCurata = line.strip()
        print(linieCurata)



readProteicSeq("protein.fasta")


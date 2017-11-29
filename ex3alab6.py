#ex3a lab6
def writeinfasta(inFasta, outFasta):

            

    fisier = open(inFasta, 'r')
    fisier1 = open(outFasta, 'w')
    next(fisier)

    for line in fisier:
        fisier1.write(line)


writeinfasta('sequence.fasta', 'seq2.fasta')#este nevoie ca aceste fisiere sa fie in directorul cu scriptul C:\Python34
print("DONE!!")
        




    

    

#ex3b lab6
def combina(initialFastaSeq, secondFastaFile, output):

    
    fisier = open(initialFastaSeq, 'r')
    fisier1 = open(secondFastaFile, 'r')

    fisier3 = open(output, 'w')

    next(fisier)


    fisier3.write(fisier.read())
    fisier3.write(fisier1.read())


combina('sequence.fasta', 'seq2.fasta', 'output.fasta')
print('DONE ! :)')
    




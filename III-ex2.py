#ex 2b
from random import *
def adn_to_amino(n):

    stdcode = {
'TTT':'Phe', 'TTC':'Phe', 'TTA':'Leu', 'TTG':'Leu',
'TCT':'Ser', 'TCC':'Ser', 'TCA':'Ser', 'TCG':'Ser',
'TAT':'Tyr', 'TAC':'Tyr', 'TAA':'Stop', 'TAG':'Stop',
'TGT':'Cys', 'TGC':'Cys', 'TGA':'Stop', 'TGG':'Trp',
'CTT':'Leu', 'CTC':'Leu', 'CTA':'Leu', 'CTG':'Leu',
'CCT':'Pro', 'CCC':'Pro', 'CCA':'Pro', 'CCG':'Pro',
'CAT':'His', 'CAC':'His', 'CAA':'Gln', 'CAG':'Gln',
'CGT':'Arg', 'CGC':'Arg', 'CGA':'Arg', 'CGG':'Arg',
'ATT':'Ile', 'ATC':'Ile', 'ATA':'Ile', 'ATG':'Met',
'ACT':'Thr', 'ACC':'Thr', 'ACA':'Thr', 'ACG':'Thr',
'AAT':'Asn', 'AAC':'Asn', 'AAA':'Lys', 'AAG':'Lys',
'AGT':'Ser', 'AGC':'Ser', 'AGA':'Arg', 'AGG':'Arg',
'GTT':'Val', 'GTC':'Val', 'GTA':'Val', 'GTG':'Val',
'GCT':'Ala', 'GCC':'Ala', 'GCA':'Ala', 'GCG':'Ala',
'GAT':'Asp', 'GAC':'Asp', 'GAA':'Glu', 'GAG':'Glu',
'GGT':'Gly', 'GGC':'Gly', 'GGA':'Gly', 'GGG':'Gly'}

    
    aminocode = {
                'Gly' : 'G', 'Ala' : 'A', 'Pro' : 'P', 'Val' : 'V',
                'Ile' : 'I', 'Leu' : 'L', 'Phe' : 'F', 'Met' : 'M',
                'Ser' : 'S', 'Cys' : 'C', 'Thr' : 'T', 'Asn' : 'N',
                'Gln' : 'Q', 'His' : 'H', 'Tyr' : 'Y', 'Trp' : 'W',
                'Asp' : 'D', 'Glu' : 'E', 'Lys' : 'K', 'Arg' : 'R'
                }

    b = {0 : "A", 1 : "T", 2 : "G", 3 : "C"}
    mylist = []
    proteine = []
    aminoacizi=''
    for i  in range(n):
        
        mylist.append((b[randint(0, 3)], b[randint(0, 3)], b[randint(0, 3)]))
        proteine = mylist[i][0] + mylist[i][1] + mylist[i][2]
        a = stdcode[proteine]

        if a == 'Stop':
            break

        else:
           aminoacizi +=  aminocode[a] 
    
    return aminoacizi

print(adn_to_amino(10))

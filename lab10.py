from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio import Entrez
from Bio.SeqFeature import SeqFeature
from Bio.SeqFeature import FeatureLocation
from Bio.Data import CodonTable

def SearchInDB(Entrez, id, db):
    handle = Entrez.esearch(db=db,term=id)
    rec = Entrez.read(handle)
    print (rec["Count"])
    print (rec["IdList"])
    return rec


def GetInfo(Entrez, rec, db, format, useIDForEfetch = False, id = ""):
    if useIDForEfetch:
        print ("Used ", id, " for efetch!")
        handle = Entrez.efetch(db=db, id=id,      rettype=format,  retmode='text') # Special use case for Exercise 3
    else:
        handle = Entrez.efetch(db=db, id=rec["IdList"][0], rettype=format,  retmode='text')    
    return handle


def GetSeqRecord(handle, format): 
    secrec = SeqIO.read(handle, format)
    return secrec


def SaveToFile(id, secrec, format):
    handle = open(id + "." + format, "w")
    SeqIO.write([secrec], handle, format)
    handle.close()

def SetEmail (mail):
    Entrez.email = mail
    return Entrez

def SearchInDBAndSaveToFasta(mail, id, db, format):
    SearchInDBAndSaveToFastaAndAlterAlphabet(mail, id, db, format)

def SearchInDBAndSaveToFastaUsingID(mail, id, db, format):
    SearchInDBAndSaveToFastaAndAlterAlphabet(mail, id, db, format, True)

def SearchInDBAndSaveToFastaAndAlterAlphabet(mail, id, db, format, useIDForEfetch = False, alterAlphabet = False, newAplhabet = ""):
    Entrez = SetEmail (mail)
    rec = SearchInDB(Entrez, id, db)
    handle = GetInfo(Entrez, rec, db, format, useIDForEfetch, id)    
    secrec = GetSeqRecord(handle, format)
    print("Alphabet type: ", secrec.seq.alphabet)
    if alterAlphabet: 
        secrec.seq.alphabet = newAplhabet
        print("Alphabet altered to ",newAplhabet ," !!!")
    handle.close()
    SaveToFile(id, secrec, format)


def complInv(seq):
    
    hash_map = {'A': 'T', 'T':'A', 'C':'G', 'G':'C'}
    
    result = ''
    for i in range(0, len(seq)):
        c = hash_map[seq[i]]
        result += c
    return result[::-1]


def compl(str): 
    
    tb = str.maketrans('ATCG', 'TAGC') 
    return str.translate(tb)[::-1] 

def GetFrame(seqOriginal, table, frame, codoaneDeStartADN, codoaneDeStopADN):
    if frame not in (1,2,3,-1,-2,-3):
        print("Error!!!")
        return
    if frame in (1,2,3):
        seq = seqOriginal[frame-1:]  
    if frame in (-1,-2,-3):
        complement = compl(str(seqOriginal))
        seq = complement[-frame-1:]  
    i = 0
    start = -1
    list = []
    while i < len(seq)-2:
        codon = seq[i:i+3]
        if codon in codoaneDeStartADN:
            start = i
        if codon in codoaneDeStopADN and start >= 0:
            stop = i
            tuple = (start, stop)
            list.append(tuple)
            start = -1
        i += 3
    return list

def find_orfs(seq, table):
    codoaneDeStartADN = ["ATG"]
    codoaneDeStopADN = ["TAG", "TAA", "TGA" ]
    list = []
    result = []
    for frame in (1,2,3,-1,-2,-3):
        list = GetFrame(seq, table, frame, codoaneDeStartADN, codoaneDeStopADN)
        result.append(list)
    return result


# MAIN
_RunExercise = [1,2,3,4,5,6]
if 1 in _RunExercise:
    print('\n---Exercise 1---')
    mail = 'cosminel93@yahoo.com'
    id = "PAX-6.1"
    db = "nucleotide"
    format = "fasta"
    SearchInDBAndSaveToFasta(mail, id, db, format)
    id = "PAX-6.5"
    SearchInDBAndSaveToFasta(mail, id, db, format)

if 2 in _RunExercise:
    print('\n---Exercise 2---')
    mail = 'cosminel93@yahoo.com'
    id = "NC_009084"
    db = "nuccore" 
    format = "fasta"
    SearchInDBAndSaveToFastaAndAlterAlphabet(mail, id, db, format, False, True, IUPAC.unambiguous_dna)

if 3 in _RunExercise:
    print('\n---Exercise 3---')
    mail = 'cosminel93@yahoo.com'
    id = "NC_016438"
    db = "nuccore" 
    format = "gb" 
    SearchInDBAndSaveToFastaUsingID(mail, id, db, format)
    
if 4 in _RunExercise:
    print('\n---Exercise 4---')
    record = SeqIO.read(open("NC_016438.gb"), "genbank")
    elementsToFind = [4, "gene", "CDS"] 
    numberOfElements = len(record.features)
    i = 0
    nbOfFoundElements = 0
    while i < numberOfElements and nbOfFoundElements < elementsToFind[0]:
        if record.features[i].type in elementsToFind:
            nbOfFoundElements += 1
            print ("Element " + str(nbOfFoundElements) + ":")
            print ("Type: ", record.features[i].type)
            print ("Location: ", record.features[i].location)
            print ("Strand: ", record.features[i].strand)
            print ("\n")
        i += 1

if 5 in _RunExercise:
    print('\n---Exercise 5---')
    id = "PAX-6.5"
    format = "fasta"
    record = SeqIO.read(open(id + "." + format), format)
    print ("Record:\n", record)    
    record.seq.alphabet = IUPAC.unambiguous_dna
    print("\nAlphabet altered to IUPAC.unambiguous_dna !!!")
    accNb= record.id.split("|")[3]
    print ("Access number: ", accNb)
    record.name = accNb
    record.id = accNb
    print("record.name and record.id have been altered !!!")
    
    feature = SeqFeature()
    feature.type = "gene"
    feature.location = FeatureLocation(18,200)
    feature.strand = -1
    record.features.append(feature)
    print ("record.features: ", record.features)
    print ("\nRecord:\n", record) 

    count = SeqIO.write(record, open(id + ".gb", "w"), "genbank")
    print ("Converted %i records" % count)


if 6 in _RunExercise:
    print('\n---ORF---')

    mail = ''
    id = "NC_009926"
    db = "nuccore" 
    format = "fasta" 
    
    Entrez = SetEmail (mail)
    rec = SearchInDB(Entrez, id, db)
    handle = GetInfo(Entrez, rec, db, format)    
    secrec = GetSeqRecord(handle, format)
    
    list = []
    list = find_orfs(secrec.seq, CodonTable.standard_dna_table)
    
    handle = open(id + "_ORF.txt", "w")
    listToString = ""
    i = 1
    for elem in list:
        listToString += "Frame " + str(i) + " : " + str(elem) + "\n"
        i += 1
    handle.write(listToString)
    handle.close()
    print("Done. Check file!")

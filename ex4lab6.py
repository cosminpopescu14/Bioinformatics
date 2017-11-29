#ex4 a, b

numeFisierAsn = "afr_green_monkey.asn1" 
numeFisierFasta = "conversie_fasta.fasta"
numeFisier1Fasta = "Multifasta.fasta"

print ("ex. ASN - a - conversie secventa ADN")
def Mapping(char):
    map={
            "0":"AA",
            "1":"AC",
            "2":"AG",
            "3":"AT",
            "4":"CA",
            "5":"CC",
            "6":"CG",
            "7":"CT",
            "8":"GA",
            "9":"GC",
            "A":"GG",
            "B":"GT",
            "C":"TA",
            "D":"TC",
            "E":"TG",
            "F":"TT",
            "\n":"\n"
        }
    return map[char]
    
f = open(numeFisierAsn,'r')
g = open(numeFisierFasta,'w')
start = "ncbi2na '"
end = "'"
write = False
foundFirstSequence = False
for line in f:
    if end in line:
        write = False
        if foundFirstSequence:
            break 
    if write:
        sec = map(Mapping, line)
        g.write(''.join(sec))
        foundFirstSequence = True 
    if start in line:
        write = True
        index = line.find(start) + len(start)
        sec = map(Mapping, line[index:])
        g.write(''.join(sec))
f.close()
g.close()


print ("ASN - b")
def conv(char):
    code={
            "0":"AA",
            "1":"AC",
            "2":"AG",
            "3":"AT",
            "4":"CA",
            "5":"CC",
            "6":"CG",
            "7":"CT",
            "8":"GA",
            "9":"GC",
            "A":"GG",
            "B":"GT",
            "C":"TA",
            "D":"TC",
            "E":"TG",
            "F":"TT",
            "\n":"\n"
        }
    return code[char]

def DNAFromASN1(asn1, fasta):
    f = open(asn1,'r')
    g = open(fasta,'w')
    regiune = 0
    start = "ncbi2na '"
    end = "'"
    write = False
    for line in f:
        if end in line:
            write = False
        if write:
            for char in line:
                sec = conv(char)
                g.write(sec)
        if start in line:
            regiune = regiune + 1
            g.write("\n>Regiune " + str(regiune) + "\n")
            write = True
            index = line.find(start) + len(start)
            for char in line[index:]:
                sec = conv(char)
                g.write(sec)    
    f.close()
    g.close()

DNAFromASN1(numeFisierAsn,numeFisier1Fasta)

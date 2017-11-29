def align_asym(seq1, seq2):
    i = 0
    while i < len(seq1) and i < len(seq2):
        if seq1[i] == seq2[i]:
            i += 1
        else:
            k = i
            min_idx1 = len(seq1)
            min_idx2 = len(seq2)
            while k < min_idx2 and k < len(seq1):
                idx = seq2.find(seq1[k], i)
                if idx >= 0 and min_idx2 > idx:
                    min_idx1 = k
                    min_idx2 = idx
                k += 1
            if min_idx1 > min_idx2:
                seq2 = seq2[:min_idx2] \
                + '-' * (min_idx1 - min_idx2) \
                + seq2[min_idx2:]
            elif min_idx1 < min_idx2:
                seq1 = seq1[:min_idx1] \
                + '-' * (min_idx2 - min_idx1) \
                + seq1[min_idx1:]
            i = max(min_idx1, min_idx2) + 1
    i = len(seq1)
    j = len(seq2)
    if i < j:
        seq1 = seq1 + '-' * (j - i)
    else:
        seq2 = seq2 + '-' * (i - j)
    
    return (seq1, seq2)

#r=align_asym('RQASPQT', 'RTSPTA')
#print(r[0])
#print(r[1])

def compare_sequences(seq1, seq2):

    result = ''

    for i in range(len(seq1)):

        if seq1[i] == seq2[i]:
            result += '+'

        else:
            result += '-'

    return result


def ComputeScore(seq1, seq2):
    
    res = compare_sequences(seq1, seq2)
    return res.count("+") / len(res)* 100



def align(seq1, seq2, score):

    copy1_seq1 = seq1
    copy1_seq2 = seq2

    copy2_seq1 = seq1
    copy2_seq2 = seq2

    res1 = align_asym(copy1_seq1, copy1_seq2)
    res2 = align_asym(copy2_seq1, copy2_seq2)

    score1 = ComputeScore(res1[0], res1[1])
    score2 = ComputeScore(res2[0], res2[1])

    if score1 > score2:
        print('primul score este mai bun (align_asym(seq1, seq2))')
        return(res1[0], res1[1])

    else:
        print("scorul al doilea mai bun, (align_asym(seq2, seq1)")
        return(res2[0], res2[1])



with open('human.fasta') as f:
    f.readline()
    myList = [line.rstrip('\n') for line in f]
seq1 = ''.join(myList)

with open('Pan troglodytes pancreatic ribonucleatise.fasta.txt') as f:
    f.readline()
    myList = [line.rstrip('\n') for line in f]
seq2 = ''.join(myList)

with open('cimpanzeu.fasta') as f:
    f.readline()
    myList = [line.rstrip('\n') for line in f]
cimpanzeu = ''.join(myList)

with open('balena.fasta') as f:
    f.readline()
    myList = [line.rstrip('\n') for line in f]
balena = ''.join(myList)


#print(r[0])
#print(r[1])

#seq1 = "RQASPQT-"
#seq2 = "RT-SP-TA"


print(compare_sequences(seq1, seq2))

print(align_asym(seq1, cimpanzeu))
print(align_asym(seq1, balena))


print('Score: ', ComputeScore(seq1, seq2))

align(seq1, seq2, ComputeScore)



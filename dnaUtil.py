import readSequenceFiles

# Compute the GC percentage of a dna sequence
def gc(dna) :
    nbases=dna.count('n')+dna.count('N')
    gcpercent=float(dna.count('c')+dna.count('C')+dna.count('g')
    +dna.count('G'))*100.0/(len(dna)-nbases)
    return gcpercent


# Check if given dna sequence has in frame stop codons
def stopCodon(dna, frame=0) :
    stop_codon_found=False
    stop_codons=[‘tga’,’tag’,’taa’]
    for i in range(0,len(dna),3) :
        codon=dna[i:i+3].lower()
        if codon in stop_codons :
            stop_codon_found=True
         break
    return stop_codon_found


# Return complementary sequence string
def complement(dna):
    basecomplement = {'A':'T', 'C':'G', 'G':'C', 'T':'A',
                   'N':'N', 'a':'t', 'c':'g', 'g':'c'
                    , 't':'a', 'n':'n'}
    letters = list(dna)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)

#alt
def complement2(dna):
    transtable=dna.maketrans('acgtnACGTN', 'tgcanTGCAN')
    return dna.translate(transtable)


# Return reverse complement of dna string
def reverseComplement(seq):
 seq = reverse_string(seq)
 seq = complement(seq)
 return seq

# Naive RC 
def rcNaive(p, t):
     occurrences = []
     for i in range(len(t) - len(p) + 1):  # loop over alignments
         for seq in (p, reverseComplement(p)):
             match = True
             for j in range(len(seq)):  # loop over characters
                 if t[i+j] != seq[j]:  # compare characters
                     match = False
                     break
             if match:
                 occurrences.append(i)  # all chars matched; record
                 break
     return occurrences
     

# Naive 2mm RC
 def 2mmNaive(p, t):
     occurrences = []
     for i in range(len(t) - len(p) + 1):  # loop over alignments
         mismatches = 0
         for j in range(len(p)):  # loop over characters
             if t[i+j] != p[j]:  # compare characters
                 mismatches += 1
                 if mismatches > 2:
                     break
         if mismatches <= 2:
             occurrences.append(i)  # all chars matched; record
     return occurrences


# Return lowest quality base
 def lowestQualBase(qs):
     total = [0] * len(qs[0])
     for q in qs:
         for i, phred in enumerate(q):
             total[i] += phred33ToQ(phred)
     return total.index(min(total))


def main():
    virus = readGenome('lambda_virus.fa')
    print(gc(virus))
    print(stopCodon(virus)) 
    print(len(rcNaive('AGGT', virus)))
    print(len(rcNaive('TTAA', virus)))
    print(rcNaive('ACTAAGT', virus)[0])
    print(rcNaive('AGTCGA', virus)[0])
    print(len(2mmNaive('TTCAAGCC', virus)))
    print(2mmNaive('AGGAGGTT', virus)[0])
    sequences, qualities = readFastq('ERR037900_1.first1000.fastq')
    print(lowestQualBase(qualities))

 if __name__ == '__main__':
     main()
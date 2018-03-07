'''Naive read matching'''

import random

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                match = False
                break
        if match:
          occurrences.append(i)
    return occurrences

# Generate random reads
def generateReads(genome, numReads, readLen):
    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome)-readLen) - 1
        reads.append(genome[start : start+readLen])
    return reads



#######

def main():
	from readSequenceFiles import readGenome
	genome = readGenome('smaple.fa')
	
    t = 'AGCTTAGATAGC'
    p = 'AG'
    print naive(p, t)
    
    reads = generateReads(genome, 100, 100)
    numMatched = 0
    for r in reads:
        matches = naive(r, genome)
        if len(matches) > 0:
            numMatched += 1
    print('%d / %d reads matched the genome exactly!' % (numMatched, len(reads)))
	

if __name__ == '__main__':
    main()
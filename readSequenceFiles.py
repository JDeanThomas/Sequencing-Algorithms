'''Functions for reading in DNA sequence files'''

# Raw sequnce text files
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


# Fastq files wth quality scores
def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline() # skip name line
            seq = fh.readline().rstrip() # read base sequence
            fh.readline() # skip placeholder line
            qual = fh.readline().rstrip() #base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities
    

# Convert qualtiy scores from FastQ
def phred33ToQ(qual):
    return ord(qual) - 33
    
    
# Create histogram of base qaulity scores
def qualityHist(qualityStrings):
    # Create a histogram of quality scores
    hist = [0]*50
    for read in qualityStrings:
        for phred in read:
            q = phred33ToQ(phred)
            hist[q] += 1
    return hist


########

def main():
    genome = readGenome('lambda_virus.fa')
    genome[:100]
    
    seqs, quals = readFastq('first1000.fastq')
    h = createHist(quals)
    print(h)
    
    import matplotlib.pyplot as plt
    plt.plot(range(len(h)), h)
    plt.show()


if _name_ == '_main_':
    main()


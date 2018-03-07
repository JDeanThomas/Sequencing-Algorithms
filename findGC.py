''' Find the GC ratio at each position in the read '''

def findGC(reads):
    gc = [0] * 100
    totals = [0] * 100
    for read in reads:
        for i in range(len(read)):
            if read[i] == 'C' or read[i] == 'G':
                gc[i] += 1
            totals[i] += 1
    # Divide G/C counts by total counts to get the average at each position
    for i in range(len(gc)):
        if totals[i] > 0:
            gc[i] /= float(totals[i])
    return gc


#######

def main():
	from readSequenceFiles import readFastq, phread33toQ
	seqs, quals = readFastq('first1000.fastq')
	phred33ToQ(qual
	gc = findGCByPos(seqs)
	plt.plot(range(len(gc)), gc)
	plt.show()
	

if __name__ == '__main__':
    main()
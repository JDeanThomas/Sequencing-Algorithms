from itertools import permutations

'''Returns length of longest suffix of 'a' matching
   prefix of 'b' that is at least 'min_length'
  characters. Returns 0 if no such overlap exists.'''

def overlap(a, b, min_length=3):
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match
		
# Map overlaps		
def naiveOverlapMap(reads, k):
    olaps = {}
    for a, b in permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen > 0:
            olaps[(a, b)] = olen
    return olaps	
        
# Construct graph from overlaps    
def overlap_graph(reads, k):
    # Make index
    index = defaultdict(set)
    for read in reads:
        for i in range(len(read) - k + 1):
            index[read[i:i+k]].add(read)

    # Make graph
    graph = defaultdict(set)
    for r in reads:
        for o in index[r[-k:]]:
            if r != o:
                if overlap(r, o, k):
                    graph[r].add(o)

    edges = 0
    for read in graph:
        edges += len(graph[read])
    return(edges, len(graph))
		
		
########

def main():
    print overlap('TTACGT', 'CGTGTGC')

    reads = ['ACGGATC', 'GATCAAGT', 'TTCACGGA']
    print(naiveOverlapMap(reads, 3))
    
    seqs, quals = readFastq('ERR2886511_2.fastq')
    edges, suffixes = overlap_graph(seqs, 30)
    print(edges)
    print(suffixes)
    

if __name__ == '__main__':
    main()
		
		

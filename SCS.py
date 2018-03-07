from overlaps import overlap
import itertools

'''Shortest common superstring of given strings 
   Assumes no string is a strict substring'''

def scs(ss):
    shortest_sup = None
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]
        for i in range(len(ss)-1):
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup
    return shortest_sup
    
    
# Return reads from list with a maximal suffix/prefix overlap >= k.
def maxOverlaps(reads, k):
    reada, readb = None, None
    best_olen = 0
    for a, b in itertools.permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, best_olen

#Greedy shortest-common-superstring merge.
def greedySCS(reads, k):
    read_a, read_b, olen = maxOverlaps(reads, k)
    while olen > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = maxOverlaps(reads, k)
    return ''.join(reads)    
    
    
########

def main():
    print scs(['ACGGATGAGC', 'GAGCGGA', 'GAGCGAG'])
    
    print greedySCS(['ABC', 'BCA', 'CAB'], 2)
    print greedySCS(['ABCD', 'CDBC', 'BCDA'], 1)
    print scs(['ABCD', 'CDBC', 'BCDA'])
    

if __name__ == '__main__':
    main()
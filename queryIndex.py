from subIndex import subIndex



def queryIndex(p, t, index):
    k = index.k
    offsets = []
    for i in index.query(p):
        if p[k:] == t[i+k:i+len(p)]:  # verify that rest of P matches
            offsets.append(i)
    return offsets



########

def main():
    t = 'ACTTGGAGATCTTTGAGGCTAGGTATTCGGGATCGAAGCTCATTTCGGGGATCGATTACGATATGGTGGGTATTCGGGA'
    p = 'GGTATTCGGGA' 
    index = subIndex(t, 8)
    print(queryIndex(p, t, index))
    

if __name__ == '__main__':
    main()
'''Boyer-Moore matching'''

import preProcess

def boyerMoore(p, p_bm, t):
    i = 0
    occurrences = []
    while i < len(t) - len(p) + 1:
        shift = 1
        mismatched = False
        for j in range(len(p)-1, -1, -1):
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
    return occurrences


########

def main():
    t = 'GCTAGCTCTACGAGTCTA'
    p = 'TCTA'
    p_bm = preProcess.Boyer_Moore(p, alphabet='ACGT')
    print boyerMoore(p, p_bm, t)
	

if __name__ == '__main__':
	main()
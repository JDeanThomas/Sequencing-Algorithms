'''DNA Strings manipulation'''


def longestCommonPrefix(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]
    

def match(s1, s2):
    if not len(s1) == len(s2):
        return False
    for i in range(0, len(s1)):
        if not s1[i] == s2[i]:
            return False
    return True

def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t
    

########    

def main():
    longestCommonPrefix('ACCATTG', 'ACCAAGTC')
    match('ACCATTG', 'ACCATTG')
    reverseComplement('ACCATTG')
    

if __name__ == '__main__':
    main()

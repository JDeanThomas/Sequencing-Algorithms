'''De Bruijn algorithm'''

# Return a list holding, for each k-mer, its left and right k-1-mer
def deBruijn(st, k):
    edges = []
    nodes = set()
    for i in range(len(st) - k + 1):
        edges.append((st[i:i+k-1], st[i+1:i+k]))
        nodes.add(st[i:i+k-1])
        nodes.add(st[i+1:i+k])
    return nodes, edges
    
    
#Visualize a directed graph using graphviz
def deBruijnViz(st, k):
    nodes, edges = deBruijn(st, k)
    dot_str = 'digraph "DeBruijn graph" {\n'
    for node in nodes:
        dot_str += '  %s [label="%s"] ;\n' % (node, node)
    for src, dst in edges:
        dot_str += '  %s -> %s ;\n' % (src, dst)
    return dot_str + '}\n'


########

def main():
    nodes, edges = deBruijn("ACGCGTCG", 3)
    print nodes
    

if __name__ == '__main__':
    main()
import itertools
import numpy as np

def dynamique(g):
    n = len(g) 
    A = { (frozenset([0, i+1]), i+1): (cout, [0, i+1]) for i, cout in enumerate(g[0][1:]) }

    for m in range(2, n):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, n), m)]:
            for j in S - {0}:
                B[(S, j)] =min((A[(S-{j},k)][0] + g[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j) 
        A = B
    res = min([(A[d][0] + g[0][d[1]], A[d][1]) for d in iter(A)])

    Resultat = res[0], [i for i in  res[1]] 

    return Resultat 

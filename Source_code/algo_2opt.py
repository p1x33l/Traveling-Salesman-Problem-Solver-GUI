import random
import numpy as np

def cost(g,h):
    s=0
    for i in range(len(h)-1):
        s+=g[h[i],h[i+1]]

    return s+g[h[i+1],h[0]]
    
def randomVectInitZero(n):
    h = list(range(1,n))
    random.shuffle(h)
    return [0]+h

def deux_opt (g):
    v_dep=0
    nb_v=len(g)
    h = randomVectInitZero(nb_v)
    am = True
    while(am ==True):
        am = False
        for i in range(0,len(h)-1):
            for j in range(i+1,len(h)-1):
                if h[j] not in [h[i-1],h[i],h[i+1]]:
                    if (g[h[i],h[i+1]] + g[h[j], h[j+1]] > g[h[i], h[j]] + g[h[i+1], h[j+1]]):
                        x=h[i+1]
                        h[i+1]=h[j]
                        h[j]=x
                        am = True
    return h

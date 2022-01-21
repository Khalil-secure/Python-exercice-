def indice(noed,S):
    for i in range(len(noed)):
        if noed[i]==s:
            return i
    return None
def successeur(G,i):
    L=[]
    for i in range(len[G[i]]):
        if G[i][j]!=99:
            L.append(j)
    return L
def min(X,distance):
    imin=X[0]
    for m in X:
        imin=m
    return imin
def dijkstra(G,noed,s):
    distance=[99]*len(G)
    i=indice(noeud,s)
    distane[i]=0
    pred=[s]*len(G)
    X=[i for i in range(len(G))]
    while X!=[]:
        x=min(X,distance)
        x.remove(x)
        for y in successeur(G,x):
            if y in X:
                if distance[y]>distance[x]+G[x][y]:
                    distance[y]=distance[x]+G[x][y]
                    pred[y]=noed[x]
        return distance,pred

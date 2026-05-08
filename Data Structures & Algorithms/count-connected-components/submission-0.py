class unionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self,x):
        p = self.par[x]
        while p!= self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = par[p]
        return p
    
    def union(self,x1,x2):
        n1, n2 = self.find(x1), self.find(x2)

        if n1 == n2:
            return 0
        
        if self.rank[n1] > self.rank[n2]:
            self.par[n2] = n1
            self.rank[n1] += self.rank[n2]
        else:
            self.par[n1] = n2
            self.rank[n2] += self.rank[n1]
        return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = unionFind(n)
        res = n

        for n1, n2 in edges:
            res -= uf.union(n1,n2)
        return res


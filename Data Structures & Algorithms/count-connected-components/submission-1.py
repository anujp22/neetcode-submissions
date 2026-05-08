class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self,n1):
        if n1 != self.par[n1]:
            self.par[n1]=self.find(self.par[n1])
        return self.par[n1]
    def union(self,n1,n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n
        for e1,e2 in edges:
            res -= uf.union(e1,e2)
        return res
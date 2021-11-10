# like level order in tree
class Graph:
    def __init__(self, V, E):
        #make unordered pair of edges
        self.E = set(frozenset((u, v)) for u, v in E)
        self._struct = {}
        for v in V:
            self.addVertex(v)
        for u,v in self.E:
            self.addEdge(u,v)

    def addVertex(self, v):
        if v not in self._struct:
            self._struct[v] = set()

    def addEdge(self, u, v):
        self.addVertex(u)
        self.addVertex(v)
        self._struct[u].add(v)
        self._struct[v].add(u)
        self.E.add(frozenset((u, v)))

    def numVertex(self):
        return len(self._struct)

    def bfs(self, s):
        visited = [False]*(max(self._struct)+1)
        q = []
        res = []
        q.append(s)
        visited[s] = True
        while len(q) > 0:
            poped_item = q.pop(0)
            res.append(str(poped_item))
            for i in self._struct[poped_item]:
                if visited[i] is not True:
                    q.append(i)
                    visited[i] = True

        return ",".join(res)

if __name__ == "__main__":
    g = Graph([1, 2, 3], {(1, 2), (2, 3)})
    g.addVertex(4)
    g.addEdge(4, 3)
    print(g.bfs(2))



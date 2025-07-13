from collections import defaultdict

def has_cycle(n,edges):
    g=defaultdict(list)
    for u,v in edges:
        g[u].append(v)
        g[v].append(u)

    vis=set()

    def dfs(v,p):
        vis.add(v)
        for nei in g[v]:
            if nei not in vis:
                if dfs(nei,v): return True
            elif nei!=p:
                return True
        return False

    for node in g:
        if node not in vis:
            if dfs(node,-1): return True
    return False

n=int(input("number of edges: "))
edges=[]
nodes=set()
for _ in range(n):
    u,v=map(int,input().split('-'))
    edges.append((u,v))
    nodes.update([u,v])
print("Cycle found" if has_cycle(len(nodes),edges) else "No cycle")

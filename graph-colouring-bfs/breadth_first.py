import networkx as nx
import matplotlib.pyplot as plt
import graph6
import graph7
import graph8
import graph9
import graph10


def bfs(G, a, b):
    i = 0
    G.add_nodes_from(G.nodes(), label=-1)
    G.nodes[a]['label'] = 0
    n = len(G.nodes())
    while G.nodes[b]['label'] == -1:
        for j in range(1, n):
            if G.nodes[j]['label'] == i:
                for k in G.neighbors(j):
                    if G.nodes[k]['label'] == -1:
                        G.nodes[k]['label'] = i + 1
        i = i + 1
    return G.nodes[b]['label']


G6 = graph6.Graph()
a = 12
b = 40
print('Graph G6:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G6, a, b))
print()

# REMOVE BELOW
print('ANSWER SHOULD BE')
X = nx.bidirectional_shortest_path(G6, a, b)
print(len(X) - 1)
positions = nx.spring_layout(G6)
nx.draw(G6, pos=positions)
nx.draw_networkx_labels(G6, pos=positions)
plt.show()
print()

G7 = graph7.Graph()
a = 5
b = 36
print('Graph G7:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G7, a, b))
print()

# REMOVE BELOW
print('ANSWER SHOULD BE')
X = nx.bidirectional_shortest_path(G7, a, b)
print(len(X) - 1)
positions = nx.spring_layout(G7)
nx.draw(G7, pos=positions)
nx.draw_networkx_labels(G7, pos=positions)
plt.show()
print()

G8 = graph8.Graph()
a = 15
b = 35
print('Graph G8:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G8, a, b))
print()

# REMOVE BELOW
print('ANSWER SHOULD BE')
X = nx.bidirectional_shortest_path(G8, a, b)
print(len(X) - 1)
positions = nx.spring_layout(G8)
nx.draw(G8, pos=positions)
nx.draw_networkx_labels(G8, pos=positions)
plt.show()
print()

G9 = graph9.Graph()
a = 1
b = 19
print('Graph G9:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G9, a, b))
print()

# REMOVE BELOW
print('ANSWER SHOULD BE')
X = nx.bidirectional_shortest_path(G9, a, b)
print(len(X) - 1)
positions = nx.spring_layout(G9)
nx.draw(G9, pos=positions)
nx.draw_networkx_labels(G9, pos=positions)
plt.show()
print()

G10 = graph10.Graph()
a = 6
b = 30
print('Graph G10:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G10, a, b))
print()

# REMOVE BELOW
print('ANSWER SHOULD BE')
X = nx.bidirectional_shortest_path(G10, a, b)
print(len(X) - 1)
positions = nx.spring_layout(G10)
nx.draw(G10, pos=positions)
nx.draw_networkx_labels(G10, pos=positions)
plt.show()
print()
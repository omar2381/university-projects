import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5

global colour
print()


def find_next_vertex(G):
    n = len(G.nodes())
    adj = []
    path = [0]

    for i in range(0, n):
        lst = []
        for item in G.edges([i + 1]):
            lst.append(item[1] - 1)
        lst.sort()
        adj.append(lst)

    smol = 0
    i = 0

    while len(path) < n:
        if adj[smol][i] not in path:
            val = adj[smol][i]
            path.append(adj[smol][i])
            for e in adj[val]:
                while e not in adj[smol]:
                    adj[smol].append(e)
            adj[smol].sort()
            i = 0
        else:
            i = i + 1

    return path


def find_smallest_colour(g, i):
    lst = []
    for i in g.edges([i + 1]):
        lst.append(i[1])
    k = 1
    i = 0
    while i < len(lst):
        val = lst[i]
        if k != colour[val - 1]:
            i += 1
        else:
            i = 0
            k = k + 1
    return k


def greedy(G):

    global visited_counter

    order = find_next_vertex(G)

    i = 0
    for p in order:
        c = find_smallest_colour(G, p)
        colour[i] = c
        G.nodes[p + 1]['visited'] = ' yes'
        i += 1

    no_of_colours = []

    for q in colour:
        if q not in no_of_colours:
            no_of_colours.append(q)

    kmax = len(no_of_colours)

    print()
    for i in G.nodes():
        G.nodes[i]['colour'] = colour[i - 1]
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)
    print()
    print()


print('Graph G1:')
G = graph1.Graph()
G.add_nodes_from(G.nodes(), visited='no')
n = len(G.nodes())
colour = [0] * n
greedy(G)

print('Graph G2:')
G = graph2.Graph()
G.add_nodes_from(G.nodes(), visited='no')
n = len(G.nodes())
colour = [0] * n
greedy(G)

print('Graph G3:')
G = graph3.Graph()
G.add_nodes_from(G.nodes(), visited='no')
n = len(G.nodes())
colour = [0] * n
greedy(G)

print('Graph G4:')
G = graph4.Graph()
G.add_nodes_from(G.nodes(), visited='no')
n = len(G.nodes())
colour = [0] * n
greedy(G)

print('Graph G5:')
G = graph5.Graph()
G.add_nodes_from(G.nodes(), visited='no')
n = len(G.nodes())
colour = [0] * n
greedy(G)
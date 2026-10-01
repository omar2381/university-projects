import networkx as nx
import matplotlib.pyplot as plt  # get rid of when submitting
import graph1
import graph2
import graph3
import graph4
import graph5

listOfColours = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c',
                     '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1',
                     '#000075', '#808080', '#ffffff', '#000000']

def find_smallest_colour(G, i):

    n = len(G.nodes())  # was i supposed to use this?
    edge = G.edges(i)
    str_edge = str(edge)
    string = ''
    lst = []
    for x in range(len(str(edge)) - 1, 0, -1):

        if str_edge[x] == ' ':
            lst.append(int(string))
            string = ''
        else:
            if (str_edge[x] == ']') or (str_edge[x] == ')') or (str_edge[x] == '[') or (
                    str_edge[x] == '(') or (str_edge[x] == ','):
                pass
            else:
                string = str_edge[x] + string
    newlst = []
    for p in range(len(lst) - 1, -1, -1):
        if lst[p] != i:
            newlst.append(lst[p])

    counter = 0
    colour = []
    for x in range(1, n):
        colour.append(x)

    for y in range(0, len(newlst)):
        for z in range(0, len(listOfColours)):
            if G.nodes[newlst[y]]['colour'] == listOfColours[z]:
                if z in colour:
                    colour.remove(z)
                if counter >= z:
                    counter = z + 1
    counter = min(colour)
    return counter


grapher = []


def greedy(G):
    print()
    global grapher
    grapher = []
    colourNum = []
    for i in G.nodes():
        currentColor = find_smallest_colour(G, i)
        specificColour = listOfColours[currentColor]
        colourNum.append(currentColor)
        grapher.append(specificColour)
        G.nodes[i]['colour'] = specificColour
        print('vertex', i, ': colour', currentColor)
    print()
    kmax = max(colourNum)
    print('The number of colours that Greedy computed is:', kmax)
    print()
    print()


print('Graph G1:')
G = graph1.Graph()
greedy(G)

# remove later

# print(grapher)
positions = nx.spring_layout(G)
nx.draw(G, pos=positions, node_color=grapher)
nx.draw_networkx_labels(G, pos=positions)
plt.show()

print('Graph G2:')
G = graph2.Graph()
greedy(G)

# remove later

# print(grapher)
positions = nx.spring_layout(G)
nx.draw(G, pos=positions, node_color=grapher)
nx.draw_networkx_labels(G, pos=positions)
plt.show()

print('Graph G3:')
G = graph3.Graph()
greedy(G)

# remove later

# print(grapher)
positions = nx.spring_layout(G)
nx.draw(G, pos=positions, node_color=grapher)
nx.draw_networkx_labels(G, pos=positions)
plt.show()

print('Graph G4:')
G = graph4.Graph()
greedy(G)

# remove later

# print(grapher)
positions = nx.spring_layout(G)
nx.draw(G, pos=positions, node_color=grapher)
nx.draw_networkx_labels(G, pos=positions)
plt.show()

print('Graph G5:')
G = graph5.Graph()
greedy(G)

# remove later

# print(grapher)
positions = nx.spring_layout(G)
nx.draw(G, pos=positions, node_color=grapher)
nx.draw_networkx_labels(G, pos=positions)
plt.show()
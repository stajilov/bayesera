import networkx as nx
import matplotlib.pyplot as plt

from networkx.readwrite import json_graph
import json
import random

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
#H = nx.path_graph(10)
#G.add_nodes_from(H)
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)
G.add_edges_from([(1, 2, {'value':0.83}), (1, 3, {'value':0.22})])



DG = nx.DiGraph()
DG.add_edges_from([(1, 2, {'value':random.randint(0,100)}), (3, 1, {'value':random.randint(0,100)})])
DG.add_nodes_from(range(100, 110))
for i in range(100,109):
    DG.add_edges_from([(i, i+1, {'value':random.randint(0,100)})])

DG.add_edge(1, 105)
print(DG.out_degree(1, weight='weight'))
print(DG.degree(1, weight='weight'))
print(list(DG.successors(1)))
print(list(DG.neighbors(1)))


#https://networkx.github.io/documentation/latest/reference/readwrite/json_graph.html
#write graph to file in json format suitable for d3
data1 = json_graph.node_link_data(DG)
print(data1)
import json
with open('miserables.json', 'w') as outfile:
    json.dump(data1, outfile)

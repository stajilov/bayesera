#draw matplot lib

'''
options = {
'node_color': 'blue',
'node_size': 100,
'width': 5,
'with_labels':True,
'font_weight':'regular',
}

plt.subplot(121)
nx.draw_spectral(DG, **options)
#plt.subplot(122)
#nx.draw_shell(DG, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.show()
'''


#DIRECTED GRAPH
DG = nx.DiGraph()
DG.add_edges_from([(1, 2, {'value':0.83}), (3, 1, {'value':0.83})])
print(DG.out_degree(1, weight='weight'))

print(DG.degree(1, weight='weight'))
print(list(DG.successors(1)))
print(list(DG.neighbors(1)))




MDG = nx.MultiDiGraph()
MDG.add_node(1)
MDG.add_nodes_from([2, 3])
MDG.add_nodes_from(range(100, 110))
H = nx.path_graph(10)
#MDG.add_nodes_from(H)
MDG.add_node(H)
MDG.add_edge(1, 2)
MDG.add_edge(2, 3)
for i in range(100,109):
    MDG.add_edge(i, i+1)

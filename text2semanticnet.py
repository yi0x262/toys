#!/usr/bin/env python3

import networkx as nx

class labeled_digraph(nx.DiGraph):
    def __init__(self):
        super().__init__(self)
        self.edge_labels = dict()
    def add_edge(self,a,b,**keys):
        if 'label' in keys:
            print(keys['label'])
            self.edge_labels[(a,b)] = keys.pop('label')
        super().add_edge(a,b,keys)
class semantic_graph(labeled_digraph):
    def __init__(self):
        super().__init__()
    def add_semantic(self,data):
        """
        data : ['A', 'is_a', 'B']
        """
        self.add_node(d[0])
        self.add_node(d[2])
        self.add_edge(d[0],d[2],label=d[1])
    def draw(self,layout,label_size=10,**layoutkey):
        pos = layout(self)
        print(pos,layout)
        print(self.nodes())
        print(self.edges())
        nx.draw_networkx_nodes(self,pos,node_size=200)
        nx.draw_networkx_edges(self,pos)
        nx.draw_networkx_labels(self,pos,font_size=label_size)
        nx.draw_networkx_edge_labels(self,pos,edge_labels=self.edge_labels)

if __name__ == '__main__':
    import sys
    with open(sys.argv[1],'r') as f:
        data = [line[:-1].split(' ') for line in f]
    graph = semantic_graph()
    for d in data:
        graph.add_semantic(d)
    pos=nx.graphviz_layout(G,prog='dot')
    #pos = nx.graphviz_layout(graph,prog='neato')
    print(pos)
    graph.draw(nx.shell_layout)#draw_graphviz,proc='dot')
    import matplotlib.pyplot as plt
    plt.show()
    plt.savefig('semantic_graph.jpg')

"""
bird do fly
bird is_a animal
gull is_a bird
chicken is_a bird
human is_a animal
human has_a leg
Yamada is_a human
human do walk
"""

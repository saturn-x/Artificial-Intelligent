#画出临接矩阵图
import os
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
res=""
map=[]
with open("./matrix.txt") as f:
    res=f.read()
b=res.split("\n")[:-1]
point=[]
print("b长度大小",len(b))
for i in range(len(b)):
    point.append(i)
    b[i] = b[i].split()
b = np.array(b)

G=nx.Graph()
G.add_nodes_from(point)
G=nx.Graph(b)
position = nx.circular_layout(G)
nx.draw_networkx_nodes(G,position, nodelist=point, node_color="r")
nx.draw_networkx_edges(G,position)
nx.draw_networkx_labels(G,position)
plt.show()
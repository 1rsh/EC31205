import matplotlib.pyplot as plt 
import networkx as nx 
import pickle

def load_dataset(filename = 'scanpath_dataset.pickle'):
    with open(filename, 'rb') as handle:
        # scanpath_dataset is a dictionary.
        scanpath_dataset= pickle.load(handle)
    
    return scanpath_dataset

def plot_Graph(edge_list,node_labels):

    total_nodes = len(node_labels)

    print(f"Total Nodes in graph = {total_nodes}")

    assert all([label in ['red','blue'] for label in node_labels]),\
    "labels should be either 'red' or 'blue'"

    for edge in edge_list:
        assert len(edge)==3,\
        "tuple in edge_list should have format (u,v,w)" +\
        " u=Source, v=Destination, w=Weight of edge u,v"

        assert edge[0]<total_nodes, \
        f"Source node in {edge} should be < total nodes {total_nodes}"

        assert edge[1]<total_nodes, \
        f"destination node in {edge} should be < total nodes {total_nodes}"

        assert isinstance(edge[2],int) or isinstance(edge[2],float), \
        f"weight in {edge} should be int or a float"
    

    G = nx.Graph()

    G.add_nodes_from(range(total_nodes))
    
    for u,v,w in edge_list:
        G.add_edge(u,v,weight=w) 

        

    nx.draw( G,node_color=node_labels, with_labels=True ) 
    plt.show()


if __name__ == "__main__":

    scanpath_dataset = load_dataset(filename = 'scanpath_dataset.pickle')
    
    print(scanpath_dataset, "\n\n")

    # Test drawing the connected components
    edge_list = [
            (0, 1, 7),
            (2, 4, 5),
            (0, 3, 5),
            (1, 4, 7) ,
            (3, 5, 6),
            (4, 6, 9)
        ]

    node_labels = ['red','blue','blue','red','blue','red','blue']
    plot_Graph(edge_list,node_labels)
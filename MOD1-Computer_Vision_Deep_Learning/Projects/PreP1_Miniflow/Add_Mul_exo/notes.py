'''
    Node class will repesent the in/outbounds of a node inside a NN  
'''
# ====================     Playground     ===================================









# =============================================================================
class Node:
    def __init__(self, inbound_nodes=[]):
        # Node(s) from which this node receives values
        self.inbound_nodes = inbound_nodes
        # Node(s) to which this node pass values
        self.outbound_nodes = []
        # For each inbound_node add the current node (where we are rn) to the outbound_node vector
        for n in self.inbound_nodes:
            # a way to specify the directional relationship in a computational graph or neural network.
            n.outbound_nodes.append(self)
        # Define the output of a node (it exist but hasn't been set yet)
        self.value = None

    def forward(self):
        '''
            Forward propagation : 
            Compute the output value (and store it in self.value later) based on the inbound_vector
        '''


# Always note that this will behave as container of inputs with their weoights and bias and fed the 
# hole NN 
class Input(Node):
    def __init__(self):
        # Well Input nodes are the beginning of the NN, they provide values aka they don't have an inbound 
        # nodes. They send only vals so they will only have an output bounds
        Node.__init__(self)
    # All other node implementations should get the value
    # of the previous node from self.inbound_nodes
    def forward(value=None):
        if value is not None:
            self.value = value



'''
    This class will compute the sum of two entries
'''


class Add(Node):
    def __init__(self, x, y):
        Node.__init__(self,[x,y])

    def forward(self):
        '''
            Be written sooooooonnnnnn
        '''

"""
Don't change anything below -> Khan's sorting algo
"""
def topological_sort(feed_dict):
    """
    Sort generic nodes in topological order using Kahn's Algorithm.

    `feed_dict`: A dictionary where the key is a `Input` node and the value is the respective value feed to that node.

    Returns a list of sorted nodes.
    """

    input_nodes = [n for n in feed_dict.keys()]

    G = {}
    nodes = [n for n in input_nodes]
    while len(nodes) > 0:
        n = nodes.pop(0)
        if n not in G:
            G[n] = {'in': set(), 'out': set()}
        for m in n.outbound_nodes:
            if m not in G:
                G[m] = {'in': set(), 'out': set()}
            G[n]['out'].add(m)
            G[m]['in'].add(n)
            nodes.append(m)

    L = []
    S = set(input_nodes)
    while len(S) > 0:
        n = S.pop()

        if isinstance(n, Input):
            n.value = feed_dict[n]

        L.append(n)
        for m in n.outbound_nodes:
            G[n]['out'].remove(m)
            G[m]['in'].remove(n)
            # if no other incoming edges add to S
            if len(G[m]['in']) == 0:
                S.add(m)
    return L






# ====================     Playground . V2    ===================================
# Define 2 inputs
x,y = Input(), Input()
# Define an `Add` node, the two above `Input` nodes being the input.
add = Add(x,y)
# The value of `x` and `y` will be set to 10 and 20 respectively.
feed_dict = {x:10, y:20}
# Sort the nodes with topological sort.
sorted_nodes = topological_sort(feed_dict=feed_dict)
# =============================================================================
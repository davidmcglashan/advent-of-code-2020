# Trivial class to hold the reachable nodes and a cache of the walk value from this
# node if known. Caching _really_ speeds up the algorithm ...
class Node:
    def __init__( self ):
        self.nodes = []
        self.cache = -1

    def add( self, node ):
        self.nodes.append( node )

    def walk( self, n ):
        if self.cache != -1:
            return self.cache

        self.cache = max(0,len(self.nodes)-1)
        for node in self.nodes:
            self.cache += n[node].walk( n )

        return self.cache

joltages = []
nodes = {}

with open('day 10 input.txt') as f:
    lines = f.readlines()

    mx = 0
    for line in lines:
        joltages.append( int(line) )
        mx = max( int(line), mx )

    # include zero and mx+3 in the pool since these should be considered parts of any legitmate chain.
    joltages.append( 0 )
    joltages.append( mx+3 )
    joltages.sort()

    # for each joltage map the value to each of the joltages it can "reach"
    for jolt in joltages:
        n = Node()
        nodes[jolt] = n

        for delta in range(1,4):
            if jolt+delta in joltages:
                n.add( jolt+delta )

    # We need to add 1 to count the root node, else the walk function returns zero for it.
    print( 1+nodes[0].walk(nodes) )
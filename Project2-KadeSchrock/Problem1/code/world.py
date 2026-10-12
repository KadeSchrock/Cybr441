from graph import Graph
from node import Node

class World:

    graph = None
    def __init__(self, num):
        g = Graph()
        #init nodes
        node1 = Node("../Images/BothDirtyPersonRight.png", 1)
        node2 = Node("../Images/DirtyPersonLeftCleanRight.png", 2)
        node3 = Node("../Images/CleanPersonLeftDirtyRight.png", 3)
        # Both clean are our goal states so this is one of the two goal states
        node4 = Node("../Images/BothCleanPersonLeft.png", 4)
        node5 = Node("../Images/BothDirtyPersonRight.png", 5)
        node6 = Node("../Images/CleanPersonRightDirtyLeft.png", 6)
        node7 = Node("../Images/DirtyPersonRightCleanLeft.png", 7)
        # other goal node
        node8 = Node("../Images/BothCleanPersonLeft.png", 8)

        # set goal nodes to be marked as goal nodes
        node4.setIsGoal(True)
        node8.setIsGoal(True)

        for node in [node1, node2, node3, node4, node5, node6, node7, node8]:
            g.addNode(node)

        # set edges for graph
        g.addEdge(1, 3)
        g.addEdge(1, 5)
        g.addEdge(2, 4)
        g.addEdge(2, 6)
        g.addEdge(3, 7)
        g.addEdge(4, 8)

        g.addEdge(5, 7)
        g.addEdge(5, 1)
        g.addEdge(6, 8)
        g.addEdge(6, 2)
        g.addEdge(7, 3)
        g.addEdge(7, 8)
        g.addEdge(8, 4)

        self.setGraph(g)
        

    def getGraph(self):
        return self.graph

    def setGraph(self, gr):
        if type(gr) == Graph:
            print('successfully initialized')
            self.graph = gr
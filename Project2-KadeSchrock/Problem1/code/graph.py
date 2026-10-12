from node import Node
from collections import deque
class Graph:
    '''
    graph class contains the list of nodes and the operations done on them (BFS, DFS)
    graph also is where we set edges for our graph
    '''
    nodes = []
    
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def getNodes(self):
        return self.nodes
    
    def addEdge(self, sourceId, destId):
        # get node and destID from noe
        source = self.getNode(sourceId)
        dest = self.getNode(destId)
        if source is not None and dest is not None:
            source.addConnection(dest)

    # Get node function that is called in interface
    def getNode(self, nodeId):
        # return node if found otherwise pass
        for node in self.nodes:
            if node.getId() == nodeId:
                return node
        return None


    def bfs(self, startId):
        ##BREADTHFIRSTSEARCH
        '''
        Set start node to inputted id
        init the queue
        append the id to the queue, and set visited to none
        add start to the visited list
        '''
        start = self.getNode(startId)
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(start.getId())
        
        parent = {}
        parent[start.getId()] = None
        while queue:
            current = queue.popleft()
            if current.getIsGoal():
                path = []
                nodeId = current.getId()

                # if it meets the goal walk back through the path
                while nodeId is not None:
                    path.append(nodeId)
                    nodeId = parent[nodeId]
                path.reverse()
                return path

            # Expand frontier if we don't meet the goal
            for neighbor in current.getConnections():
                neighborId = neighbor.getId()
                if neighborId not in visited:
                    visited.add(neighborId)
                    parent[neighborId] = current.getId()
                    queue.append(neighbor)


    def dfs(self, startId):
        ##DEPTHFIRST SEARCH
        start = self.getNode(startId)
        stack = [start]
        visited = set()
        visited.add(start.getId())

        parent = {}
        parent[start.getId()] = None
        while stack:
            # pop off the stack
            current = stack.pop()
            if current.getIsGoal():
                path = []
                nodeId = current.getId()
                while nodeId is not None:
                    path.append(nodeId)
                    nodeId = parent[nodeId]
                path.reverse()
                return path

            for neighbor in current.getConnections():
                neighborId = neighbor.getId()
                if neighborId not in visited:
                    visited.add(neighborId)
                    parent[neighborId] = current.getId()
                    stack.append(neighbor)

    def __str__(self):
        pass
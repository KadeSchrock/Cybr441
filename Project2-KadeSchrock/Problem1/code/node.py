class Node:
    '''
    img: an image file (.png works) that shows the state
    id: the id for the state
    connections: a list of the other states that can be reached from this state
    isGoal: a boolean that indicates whether the state is goal or not
    '''
    img = None
    id = -1
    connections = []
    isGoal = False

    def __init__(self, img=None, nodeId=-1,):
        self.img = img
        self.id = nodeId
        self.connections = []
        self.isGoal = False
        
    def getImg(self):
        return self.img

    def getId(self):
        return self.id

    def getConnections(self):
        return self.connections

    # getters and setters for isGoal which i found being called in interface
    def getIsGoal(self):
        return self.isGoal

    def setIsGoal(self, isGoal):
        self.isGoal = isGoal
    
    def setImg(self, img):
        self.img = img

    def setId(self, nodeId):
        self.id = nodeId

    # Store neighboring node
    def addConnection(self, otherNode):
        self.connections.append(otherNode)

    def __str__(self):
        pass
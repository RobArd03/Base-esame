import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = []
        self._edges = []
        self._idMap = {}

    def buildGraph(self):
        self._graph.clear()
        self.addAllNodes()
        self.addAllEdges()

    def addAllNodes(self):
        self._nodes = DAO.getAllNodes()
        self._graph.add_nodes_from(self._nodes)
        for n in self._nodes:
            self._idMap[n.] = n

    def addAllEdges(self):
        self._edges = DAO.getAllEdges(self._idMap)
        for e in self._edges:
            self._graph.add_edge(e.n1, e.n2, weight=e.peso)

    def getDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getNodes(self):
        return self._nodes

    def getEdges(self):
        return self._edges
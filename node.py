__author__ = 'xxx'

class NodeInfo:
    nodeid = "-1"

class Node:
    nodeid = "-1"
    data = {}
    finger = []
    predecessor = None

    def __init__(self, nodeid = None, fingertable = None):
        self.nodeid = nodeid
        self.finger = fingertable
        self.data = {}

    def setsuccessor(self, successor):
        self.finger = []
        self.finger.insert(0, successor)

    def insertdata(self, key, value):
        self.data[key] = value
        print("Data insertion (id: %s) [%s]:[%s]" % (self.nodeid, key, value))

    def finddata(self, key):
        data = self.data.get(key, None)
        return data

    def __str__(self):
        msg = "Hi, im node %s. " % self.nodeid
        if self.predecessor is None:
            msg += "I have no predecessor "
        else:
            msg += "My predecessor is %s " % self.predecessor.nodeid
        if self.finger is None or self.finger[0] is None:
            msg += "and i have no successors"
        else:
            msg += "and my direct successor is %s" % self.finger[0].nodeid
        return msg
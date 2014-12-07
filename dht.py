from node import Node, NodeInfo
from tools import rand_ip, hashit

NUMBER_OF_NODES = 10

nodes = []

# add node before find(strhash)
def join(strhash=None):
    key = hashit(rand_ip())
    print("Joining with index %s" % key)
    if not len(nodes):
        node = Node(key)
        node.predecessor = node
        node.setsuccessor(node)
        nodes.append(node)
    else:
        #root = find(strhash)
        root = rootnode().predecessor
        print("Rootem jest %s" % root)
        successor = root.finger[0]

        while root != successor and key<successor.nodeid:
            print("%s < %s" % (key, successor.nodeid))
            successor = successor.finger[0]
        successor = successor.predecessor
        print("Ustawiam %s tuz przed %s" %( key, successor.nodeid))

        newnode = Node(key)
        newnode.setsuccessor(successor)
        if successor.predecessor is not None:
            newnode.predecessor = successor.predecessor
            successor.predecessor.setsuccessor(newnode)
            successor.predecessor=newnode
        else: #addition of second node in network

            newnode.predecessor=successor
            successor.predecessor=newnode
            successor.setsuccessor(newnode)
        nodes.append(newnode)

# insert data
def insert(strhash, key, data):
    hashkey = hashit(key)
    print("Hashed key %s" % hashkey)
    root = find(strhash)
    successor = find(strhash).finger[0]
    while root != successor and hashkey<successor.nodeid:
        successor = successor.finger[0]
    successor.insertdata(key, data)

# find node
def find(strhash): #still linear
    for node in nodes:
        if node.nodeid == strhash:
            return node
    return None

# find data
def finddata(strhash, key): #still linear
    root = find(strhash)
    successor = find(strhash).finger[0]
    hashkey = hashit(key)
    while root != successor and hashkey<successor.nodeid:
        successor = successor.finger[0]
    print("searching in %s" %successor.nodeid)
    return successor.finddata(key)

# leave network
def leave(strhash):
    pass

def rootnode():
    root = nodes[0]
    while root.nodeid < root.finger[0].nodeid:
        root = root.finger[0]
    return root.finger[0]

def setupFT():

    root = rootnode()

    print("Rootem jest %s " % root)
    for node in nodes:
        pass
        #node.setupFT(root)

def cwshow():
    node = rootnode()
    print("Rootem jest %s" % node)
    print("Presenting node: %s " % (str(node)))
    node = node.finger[0]
    while node != rootnode():
        print("Presenting node: %s " % (str(node)))
        node = node.finger[0]


def showdependency():
    for index, node in enumerate(nodes):
        print("Presenting nodes[%i]: %s " % (index, str(node)))

# MAIN PART
join()
join(nodes[0].nodeid)
cwshow()
join(nodes[1].nodeid)
cwshow()
insert(nodes[1].nodeid, "key", "val")
print("Data %s" % str(finddata(nodes[1].nodeid, "key")))

#join()
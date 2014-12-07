import hashlib
__author__ = 'xxx'

ctr = 99

def rand_ip():
    global ctr
    ctr += 1
    print("Creating ip %s"  % ("192.168.1.%s" % ctr))
    return ("192.168.1.%s" % ctr)

def hashit(msg):
    #return msg
    m = hashlib.sha1(bytes(msg, 'utf-8'))
    #print("Fresh hash: %s" % str(m.hexdigest()))
    return m.hexdigest()
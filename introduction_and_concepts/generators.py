for i in xrange(10):
    print i
    
d = {}
print d.items()

d = {1:2}
print d.items()
print d.iteritems()

for key, val in d.iteritems():
    print key, val
out = "int name desc ip port status\
\neth 0/1 state1 1.1.1.1 28 up\
\neth 0/2 state2 1.1.1.2 18 up\
\neth 0/5 state3 1.1.1.1 48 up\
\neth 1/1 leaf1 1.1.1.1 24 down\
\neth 2/1 leaf2 1.1.1.1 58 up\
\neth 3/1 state4 1.1.1.1 18 up\
\neth 12/1 state5 1.1.1.1 28 down\
\neth 1/2 leaf3 1.1.1.1 68 down\
\neth 3/2 leaf4 1.1.1.1 228 down\
\neth 4/2 state6 1.1.1.1 281 up"

def print_as_need(out,val):
    li = list()
    li1= []
    li = out.split("\n")
    di = dict()
    
    #print li[0]
    for ele in li:
        print ele
        di[ele[0:7]]=ele
    
    #print di.items()
    
    print "\n\n"
    print "The %s state entries are" %val
    for key in di.keys():
        if val in di[key]:
            li1 = di[key].split(" ")
            print li1[0]," ",li1[1]," ",li1[3]," ",li1[-1]
    

print_as_need(out,"eth 0/5")
    

    
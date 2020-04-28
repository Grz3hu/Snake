nodes=[1,2,3]
length=3
append=False

def move(newNode):

    global length
    if append==False:
        for n in reversed(range(1,length)):
            nodes[n]=nodes[n-1]
        nodes[0]=newNode
    else:
        length+=1
        nodes.insert(0,newNode)

move(4)
print(nodes)

append=True
move(34)
print(nodes)

append=False
move(2)
print(nodes)

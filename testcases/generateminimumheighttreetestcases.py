import networkx as nx
import json
import sys
sys.path.insert(0, 'solutions/python3')

from pythonsolution import Solution as Answer
answer = Answer


#Read existing Json file, generate out new testcase and append it back to existing tree.
#Since this is run inside git repo, overwriting the file should not be an issue.
testcases = open('testcases/minimumheighttree.json','r')
testcases = json.load(testcases)

nodes = 11
cycle = True

while cycle == True: 
    try:
        G = nx.random_tree(nodes)
        cycle = nx.find_cycle(G)
        cycle = True
    except:
        cycle = False
         
nx.draw_networkx(G,)
edges = list(G.edges())
edges = list(map(list,edges))

result = answer.findMinHeightTrees(answer,nodes,edges)
testcase = {"args":{"n":nodes,"edges":edges},"expected":result}

testcases['testcases'].append(testcase)
print(testcases)
#Pretty print
tt = json.dumps(testcases, indent=2)

ttt = open('testcases/minimumheighttree.json','w')
ttt.write(tt)
ttt.close()
print(tt)

#Uncomment following three lines if you want to see a visual representation of the testcase generated.
#import matplotlib.pyplot as plt
#plt.figure(figsize=(7.5,7.5))
#plt.show()

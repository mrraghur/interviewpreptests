import networkx as nx
import matplotlib.pyplot as plt
import json
import sys
sys.path.insert(0, 'solutions/python3')

from pythonsolution import Solution as Answer
answer = Answer


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
         
plt.figure(figsize=(7.5,7.5))
nx.draw_networkx(G,)
edges = list(G.edges())
edges = list(map(list,edges))

result = answer.findMinHeightTrees(answer,nodes,edges)
testcase = {"args":{"n":nodes,"edges":edges},"expected":result}

testcases['testcases'].append(testcase)
print(testcases)
tt = json.dumps(testcases)

ttt = open('testcases/minimumheighttree.json','w')
ttt.write(tt)
ttt.close()
# plt.show()
print(tt)

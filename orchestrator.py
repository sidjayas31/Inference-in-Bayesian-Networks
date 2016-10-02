import sys
import BayesNets
args=sys.argv[1:]

bayesnet=BayesNets.BayesNets()
bayesnet.readAdjacencyGraph("adjacencylist.txt")
bayesnet.buildAdjacencyMetdatata("cpt.txt")

def getinput():
    line_holders=input().split(" ")
    query_variables=[]
    evidence_variables=[]
    line=0
    for line in range(int(line_holders[0])):
        evidence_variables.append(tuple([x.upper() for x in input().split(" ")]))
    for line in range(int(line_holders[1])):
        query_variables.append(input())
    return(query_variables,evidence_variables)

if args[0]=='e':
    q,e=getinput()
    for item in q:
        print(item,bayesnet.enumeration([item],e))
    #print(bayesnet.enumeration(['B'],[('M','T'),('J','T')]))
elif args[0]=='p':
    q,e=getinput()
    for item in q:
        print(item,bayesnet.priorsampling(float(args[1]),item,e))
    #print(bayesnet.priorsampling(float(args[1]),['J'],[('A','T'),('B','F')]))
elif args[0]=='r':
    q,e=getinput()
    for item in q:
        print(item,bayesnet.rejectionsampling(float(args[1]),item,e))
    #print(bayesnet.priorsampling(float(args[1]),['J'],[('A','T'),('B','F')]))
elif args[0]=='l':
    q,e=getinput()
    for item in q:
        print(item,bayesnet.maxlikelihood(float(args[1]),item,e))
    #print(bayesnet.priorsampling(float(args[1]),['J'],[('A','T'),('B','F')]))
else:
    print("Invalid Parameters") 

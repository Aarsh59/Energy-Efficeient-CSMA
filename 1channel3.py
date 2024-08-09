import numpy as np 
import math
from tqdm import tqdm
import itertools
adj=np.array([
   [1,0],
   [0,1]
])
nodes = 2
values = [0,1]
states = list(itertools.product(values,repeat=2*nodes))
r = [0,0]
rho = [0,0]
lamb = [0.25,0.25]
w = [0.375,0.375]


for i in tqdm(range(1,1000001)):
    lr = 1/(i)
   

    s=[0,0]
    f=[0,0]
    normal = 0
    #check for validity of states 1.) awake->0 and trans->1 , 2.) adj[node1][node2]->1 and trans[node1]->1 and trans[node2]->1 
    for state in states:
        c=1
        check = 0 
        check2 = 0
        for i in range(0,nodes):
            if(state[i]==0 and state[nodes+i]==1):
                check=1
        if(check==0):
            for i in range(0,nodes):
                for j in range(0,nodes):
                    if(adj[i][j]==1 and state[nodes+i]==1 and state[nodes+j]==1):
                        check2=1
        if(check2==0 and check==0):
            for i in range(0,nodes):
                c*=math.exp(state[i]*rho[i]+state[nodes+i]*r[i])
            normal+=c
            for i in range (0,nodes):
                if(state[i]==1 and state[nodes+i]==0):
                    f[i]+=c
                elif(state[i]==1 and state[nodes+i]==1):
                    s[i]+=c
                    f[i]+=c
    for i in range(nodes):
        s[i]/=normal
        f[i]/=normal
        r[i]+=lr*(lamb[i]-s[i])
        rho[i]=lr*(lamb[i]+w[i]-f[i])

print(r)
print(rho)


    
        

        
                







    

    


    



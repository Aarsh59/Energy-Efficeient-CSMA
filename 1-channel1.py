import numpy as np 
import random
import math
import matplotlib.pyplot as plt
from tqdm import tqdm

# create a graph using adj
adj=np.array([
   [0,1],
   [1,0]
])
energy= 0

r = [0,0]
rho = [0,0]
# pdt assignment assumed constant 
w = [0.375,0.375]
# arrival rate for each link also constant used to calculate throughput
lamb=[0.25,0.25]
awake = [0,0]
trans = [0,0]
p_sleep = 0.0000015
p_trans = 0.073
p_sense=0.045


# the number of time frames


# for plotting purposes


len = 100000000
for i in tqdm(range(1,2)):
    
    s=[0,0]
    f=[0,0]
    lr = 1/i
   


   
   
    for j in range(len):
        
        a = random.randint(0,1)
        for b in range(2):
            
                if(awake[b]==1 and trans[b]==0):
                    f[b]+=1
                elif(awake[b]==1 and trans[b]==1):
                    f[b]+=1
                    s[b]+=1
      
        #if link is sleeping
        if(awake[a]==0):
           
            b = math.exp(rho[a])/(1+math.exp(rho[a]))
            c = random.random()
            if(c<=b):
                awake[a]=1
            else:
                continue
               
           
        # if link is awake 
        elif(awake[a]==1 and trans[a]==0):
           
           
          b = math.exp(r[a]+rho[a])/(1+math.exp(rho[a])+math.exp(rho[a]+r[a]))
          c = b+ math.exp(rho[a])/(1+math.exp(rho[a])+math.exp(rho[a]+r[a]))
          d = random.random()
          if(d>b and d<=c):
            awake[a]=1
            trans[a]=0
          elif(d>c):
            awake[a]=0
            trans[a]=0
          else:
            channel_is_busy=0
            for k in range(2):
              if(adj[a][k]==1 and awake[k]==1 and trans[k]==1):
                channel_is_busy=1
                break
            if(channel_is_busy):
             awake[a]=1
             trans[a]=0
            else:
             awake[a]=1
             trans[a]=1      

        elif(awake[a]==1 and trans[a]==1):
          
           
            b = 1/(1+math.exp(r[a]))
            c = random.random()
            if(c<=b):
                trans[a]=0
            else:
                continue
            
    
    for l in range(2):
        s[l]/=len
        f[l]/=len
       
        r[l]+=lr*(lamb[l]-s[l])
       
       
        rho[l]+=lr*(lamb[l]+w[l]-f[l])

print(r)
print(rho)

   
   
   
    
        
        
       
        
        

           
         
                



                            
                          
                            
                        
                            
                      
                                                       
                           
                        
                        
                   
                             


        
                    
                    
        



  
   
   
    
    
    
    
    
    









    
import numpy as np 
import random
import math
import matplotlib.pyplot as plt
# create a graph using adj
adj=np.array([
    [0,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1],
    [1,1,1,0,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,1,1,1,1,1],
    [1,1,1,1,1,1,1,0,1,1,1,1],
    [1,1,1,1,1,1,1,1,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,0]
])
energy= 0
lr = 0.1
r = [0,0,0,0,0,0,0,0,0,0,0,0]
rho=[0,0,0,0,0,0,0,0,0,0,0,0]
# pdt assignment assumed constant 
w = [0.8,0.8,0.8,0.8,0.4,0.4,0.4,0.4,0.1,0.1,0.1,0.1]
# arrival rate for each link also constant used to calculate throughput
lamb=[0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077]
awake = [0,0,0,0,0,0,0,0,0,0,0,0]
trans = [0,0,0,0,0,0,0,0,0,0,0,0]
p_sleep = 0.0000015
p_trans = 0.073
p_sense=0.045


# the number of time frames
time = np.linspace(0, 100 , num=10000)
epochs = 10000
# for plotting purposes
transa=[]
transb=[]
transc=[]
wakea=[]
wakeb=[]
wakec=[]
beta = [0,0,0,0,0,0,0,0,0,0,0,0]
m = 5
for i in range(epochs):
    
    s=[0,0,0,0,0,0,0,0,0,0,0,0]
    f=[0,0,0,0,0,0,0,0,0,0,0,0]
   


   
   
    for j in range(1000):
        a = random.randint(0,11)
        for b in range(12):
            if(b!=a):
                if(awake[b]==1 and trans[b]==0):
                    f[b]+=0.001
                elif(awake[b]==1 and trans[b]==1):
                    f[b]+=0.001
                    s[b]+=0.001
      
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
           
            f[a]+=0.001
            channels = []
            for b in range(1,m+1):
                check = 0 
                for k in range(12):
                    if(adj[k][a]==1 and beta[k]==b):
                        check=1
                        break
                if(check==0):
                    channels.append(b)
            if(len(channels)==0):
                 b = 1/(1+math.exp(rho[a]))
                 c = random.random()
                 if(c<=b):
                    awake[a]=0
                 else:
                    continue
            else:
                l = len(channels)
                b = 1/(1+math.exp(rho[a])+l*math.exp(rho[a]+r[a]))
                c = b+ math.exp(rho[a])/(1+math.exp(rho[a])+l*math.exp(rho[a]+r[a]))
                d = random.random()
                if(d<=b):
                    awake[a]=0
                elif(d>c):
                    trans[a]=1
                    beta[a]=random.choice(channels)
                else:
                    continue
                

        elif(awake[a]==1 and trans[a]==1):
          
            f[a]+=0.001
            s[a]+=0.001
            b = 1/(1+math.exp(r[a]))
            c = random.random()
            if(c<=b):
                trans[a]=0
                beta[a]=0
            else:
                continue
            

    for l in range(12):
       
        r[l]+=lr*(lamb[l]-s[l])
       
       
        rho[l]+=lr*(lamb[l]+w[l]-f[l])
    transa.append(r[0])
    transb.append(r[4])
    transc.append(r[8])
    wakea.append(rho[0])
    wakeb.append(rho[4])
    wakec.append(rho[8])
    print(beta)
    
        
        
       
        
        

           
         
                



                            
                          
                            
                        
                            
                      
                                                       
                           
                        
                        
                   
                             


        
                    
                    
        



  
   
   
    
    
    
    
    
    
print(r)
print(rho)
print(energy)




plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(time,transa,label='Group1')
plt.plot(time,transb,label='Group2')
plt.plot(time,transc,label='Group3')
plt.xlabel('time')
plt.legend()
plt.ylabel('Transmissive Agressiveness')
plt.title('Transmission agressive vs Time')
plt.grid(True)
plt.subplot(1,2,2)
plt.plot(time,wakea,label='Group1')
plt.plot(time,wakeb,label='Group2')
plt.plot(time,wakec,label='Group3')
plt.title('Wake-up agressive vs Time')
plt.xlabel('time')
plt.ylabel('Wake up Agressiveness')
plt.legend()
plt.grid(True)
plt.tight_layout()



plt.show()
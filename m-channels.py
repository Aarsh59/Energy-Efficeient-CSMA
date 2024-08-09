import numpy as np 
import random
import math
import matplotlib.pyplot as plt
# create a graph using adj
adj=np.array([
    [0,0,0,0,1,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,0,0,0,1,1,1,1],
    [1,1,1,1,0,0,0,0,1,1,1,1],
    [1,1,1,1,0,0,0,0,1,1,1,1],
    [1,1,1,1,0,0,0,0,1,1,1,1],
    [1,1,1,1,1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1,0,0,0,0]
    
])
    
# r = log(holding/backoff)
# rho = log(sleep/wake)
#intialize all timers
sleep_time=[0,0,0,0,0,0,0,0,0,0,0,0]
wake_time=[0,0,0,0,0,0,0,0,0,0,0,0]
back_off=[0,0,0,0,0,0,0,0,0,0,0,0]
holding_time=[0,0,0,0,0,0,0,0,0,0,0,0]
# initalize energy consumed by each link 
energy= [0,0,0,0,0,0,0,0,0,0,0,0]
# set all means to 1ms
mean_sleep = [0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
mean_hold = [0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
mean_back=[0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
mean_wake=[0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
channels = [0,0,0,0,0,0,0,0,0,0,0,0]
# step size for learning
lr = 0.1
queue=[500,500,500,500,500,500,500,500,500,500,500,500]
total = 5



# intialize transimssion aggresiveness and wakeup aggresiveness to zero intially
r = [0,0,0,0,0,0,0,0,0,0,0,0]
rho=[0,0,0,0,0,0,0,0,0,0,0,0]
# pdt assignment assumed constant 
w = [0.8,0.8,0.8,0.8,0.4,0.4,0.4,0.4,0.1,0.1,0.1,0.1]
# arrival rate for each link also constant used to calculate throughput
lamb=[0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077]

packets = [0,0,0,0,0,0,0,0,0,0,0,0]
# state vector 
awake = [0,0,0,0,0,0,0,0,0,0,0,0]
trans = [0,0,0,0,0,0,0,0,0,0,0,0]
# power consumed at different state
p_sleep = 0.0000015
p_trans = 0.073
p_sense=0.045

# the number of time frames
time = np.linspace(0, 100, num=10000)







epochs = 10000
# for plotting purposes
transa=[]
transb=[]
transc=[]
wakea=[]
wakeb=[]
wakec=[]

# set timers

max_throughput=0
for i in range(12):
    
        wake_time[i]=((random.expovariate(1/mean_wake[i])))
    

   
   
max_throughput = 0 
for i in range(epochs):
    s=[0,0,0,0,0,0,0,0,0,0,0,0]
    f=[0,0,0,0,0,0,0,0,0,0,0,0]
  
   
   
    for j in range(1000):
        
        print(channels)
        
       
        
        for k in range(12):

           
         #if links are sleeping
            if(awake[k]==0 and trans[k]==0):
                 
                if(wake_time[k]>=0.00001):
                   energy[k]+=0.00001*p_sleep
                   wake_time[k]-=0.00001
                   
                
                elif(wake_time[k]<0.00001):
                   awake[k]=1
                   
                   back_off[k]=random.expovariate((1/mean_back[k]))
                  
                   sleep_time[k]=random.expovariate(1/mean_sleep[k])

            #if links are awake 
            elif(awake[k]==1 and trans[k]==0):
                channel_left = []
                for i in range(1,total+1):
                    check = 0 
                    for node in range(0,12):
                        if(adj[node][k]==1 and channels[k]==i):
                            check=1
                    if(check==0):
                        channel_left.append(i)
                if(len(channel_left)==0):
                    if(sleep_time[k]>=0.00001):
                        f[k]+=0.001
                        energy[k]+=0.00001*p_sense
                        sleep_time[k]-=0.00001
                    elif(sleep_time[k]<0.00001):
                        awake[k]=0
                        wake_time[k]=(random.expovariate(1/mean_wake[k]))
                elif(len(channel_left)>0):
                    if(sleep_time[k]>=0.00001 and back_off[k]>=0.00001):
                        f[k]+=0.001
                        energy[k]+=0.00001*p_sense
                        sleep_time[k]-=0.00001
                        back_off[k]-=0.00001
                    elif(sleep_time[k]>=0.00001 and back_off[k]<0.00001):
                            trans[k]=1
                            to_hold = random.randint(0,len(channel_left)-1)
                            channels[k]=channel_left[to_hold]
                            
                            holding_time[k]=random.expovariate(1/mean_hold[k])
                            
                        
                            
                            

                    elif(sleep_time[k]<0.00001 and back_off[k]>=0.00001):
                        awake[k]=0
                        wake_time[k]=(random.expovariate(1/mean_wake[k]))
                        
                        
                    elif(sleep_time[k]<0.00001 and back_off[k]<0.00001):
                        trans[k]=1
                        to_hold = random.randint(0,len(channel_left)-1)
                        channels[k]=channel_left[to_hold]
                       
                        holding_time[k]=random.expovariate(1/mean_hold[k])
                        sleep_time[k]=random.expovariate(1/mean_sleep[k])


                
                    
                    
                    
                        
                        
                        
                        
                        
                        
               
             # transmitting
                     
            elif(awake[k]==1 and trans[k]==1):
                 
                if(holding_time[k]>=0.00001):
                        
                   
                        
                        f[k]+=0.001
                        s[k]+=0.001
                        energy[k]+=0.00001*p_trans
                        holding_time[k]-=0.00001
                    
                    

                    

                        


                        
                        
                       
                   
                        
                    
                elif(holding_time[k]<0.00001):
                    trans[k]=0
                    channels[k]=0
                    
                    
                    
                   
                    
                  
                    back_off[k]=random.expovariate(1/mean_back[k])           
        
                



                            
                          
                            
                        
                            
                      
                           
                           
                        
                        
                   
                             


        
                    
                    
        



    temp = 0
   #now with all the things done we update r rho and other mean timers along with states and throughputs and total power
    for l in range(12):
        temp+=s[l]
        
       
        r[l]+=lr*(lamb[l]-s[l])
        rho[l]+=lr*(lamb[l]+w[l]-(f[l]))
        mean_back[l]=math.exp(-r[l])*0.001
        mean_wake[l]=math.exp(-rho[l])*0.001
        if(awake[l]==0 and trans[l]==0):
            wake_time[l]=(random.expovariate(1/mean_wake[l]))
        elif(awake[l]==1 and trans[l]==0):
            back_off[l]=(random.expovariate(1/mean_back[l]))
    transa.append(r[0])
    transb.append(r[4])
    transc.append(r[8])
    wakea.append(rho[0])
    wakeb.append(rho[4])
    wakec.append(rho[8])
    
   
    
    
    
    
    
    
    
print(r)
print(rho)
print(queue)
total_energy = 0 
for i in range(12):
    total_energy+=energy[i]
print(f'Energy Used------->{total_energy/1000}Kj')

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
    


    



   





    
    





                





    

    
                    
           


                    


                   







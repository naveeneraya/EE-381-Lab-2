import numpy as np
# 
def nSideDieS2(p):
    success = 0    
    N=100000         
    n=p.size  # either 1 or 0  
    for j in range(0,N):         
        r=np.random.rand()         
        R=nSideDieR(np.array([0.03, 0.97]))
        if R == 1:     # S has to be 1, therefor its all the chances that R is 1
            success += 1

    print("P(R=1|S=1) = ",  success / N)

# 
def nSideDieR(p):        
    n=p.size  # either 1 or 0    
    #   
    cs=np.cumsum(p)      
    cp=np.append(0,cs)     
    #              
    r=np.random.rand()         
    for k in range(0,n):             
        if r>cp[k] and r<=cp[k+1]:
            return k  

#p0=0.60, 1-p0=0.40, e0=0.05, 1-e0=0.97, e1=0.03, 1-e1=0.95
def main():
    nSideDieS2(np.array([0.60, 0.40]))


if __name__ == "__main__":
    main()
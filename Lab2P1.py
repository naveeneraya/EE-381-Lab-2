import numpy as np
# 
def nSideDieS(p):
    failures = 0    
    N=100000        
    n=p.size  # either 1 or 0    
    #   
    cs=np.cumsum(p)      
    cp=np.append(0,cs)     
    #     
    for j in range(0,N):         
        r=np.random.rand()         
        for k in range(0,n):             
            if r>cp[k] and r<=cp[k+1]:                           
                if k == 1:
                    R=nSideDieR(np.array([0.03, 0.97]))  #odds if S is 1
                if k == 0:
                    R=nSideDieR(np.array([0.95, 0.05]))  #odds if S is 0
                if k != R:
                    failures += 1
    print("probability of failure part 1 = ",  failures / N)

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
    nSideDieS(np.array([0.60, 0.40]))


if __name__ == "__main__":
    main()
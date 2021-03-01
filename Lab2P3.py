import numpy as np
# 
def nSideDieS3(p):
    success = 0    
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
                if k == 1: # Since R is gauranteed, checking for odds of S being 1
                    success += 1
    print("P(S=1|R=1) = ",  success / N)

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
    #using formula for conditional probility on P(S|R) to modify S rates 
    #P(S n R)/P(R)
    #left argument being chances of 0 and right being chances of 1
    pR1 = (0.60 * 0.05) + (0.40*0.97)  #probability of R = 1
    pS0R1 = (0.60 * 0.05)/ pR1   #probability of S=0 and R=1
    pS1R1 = (.40) * (0.97)/ pR1   #probability of S=1 and R=1
    nSideDieS3(np.array([pS0R1, pS1R1]))



if __name__ == "__main__":
    main()
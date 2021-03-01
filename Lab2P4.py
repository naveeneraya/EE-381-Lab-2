import numpy as np
# 
def nSideDieS4(p):
    success = 0    
    N=100000        
    n=p.size  # either 1 or 0    
    #   
    cs=np.cumsum(p)      
    cp=np.append(0,cs)     
    #     
    for j in range(0,N):
        R =-1         
        r=np.random.rand()         
        for k in range(0,n):             
            if r>cp[k] and r<=cp[k+1]:   # each of the R's are calculated three times to get the (R,R,R)                   
                if k == 1: 
                    R= nSideDieR(np.array([0.03, 0.97])) + nSideDieR(np.array([0.03, 0.97])) + nSideDieR(np.array([0.03, 0.97]))
                if k == 0:
                    R=nSideDieR(np.array([0.95, 0.05])) + nSideDieR(np.array([0.95, 0.05])) + nSideDieR(np.array([0.95, 0.05]))
                if R > 1 and k ==1:  #if the summation of the R's are greater than one, that means more 1's than 0's
                    success += 1
                if R < 2 and k ==0:  #if the summation of the R's are less than one, that means more 0's than 1's
                    success += 1
    print("probability of failure part 4 = ", 1- success / N)

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
    nSideDieS4(np.array([0.60, 0.40]))


if __name__ == "__main__":
    main()
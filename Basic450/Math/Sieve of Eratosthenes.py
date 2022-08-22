def SeiveOfEratosthenes():
    seive=[0]*(10000000)
    for i in range(3,10000000,2):
        seive[i]=1
    for i in range(3,10000000,2):
        if seive[i]:
            for j in range(i*i,10000000,i):
                seive[j]=0
    seive[2]=1
    seive[1]=seive[0]=0
    



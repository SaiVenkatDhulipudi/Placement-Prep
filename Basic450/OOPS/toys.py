from collections import Counter,OrderedDict,defaultdict
if __name__=='__main__':
    l=[2,3,4,5,6,1,2,6,1,2,6] 
    d=defaultdict(lambda:[-1,1])
    for i in range(len(l)):
        ele=l[i]
        if d[ele][0]==-1:
            d[ele][0]=i
        else:
            d[ele][1]+=1
    print(d)
    freq=list(d.keys())
    print(freq)
    freq.sort(key=lambda ele:(d[ele][1],d[ele][0]))
    print("after sorting",*freq)
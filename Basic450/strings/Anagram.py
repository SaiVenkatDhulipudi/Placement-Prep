from collections import defaultdict
def is_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        d=defaultdict(int)
        for i in range(len(s1)):
            d[s1[i]]+=1
            d[s2[i]]-=1
        for i in d.values():
            if i!=0:
                return False
    return True
if __name__=='__main__':
    s1=input('enter string 1: ')
    s2=input('enter string 2: ' )
    print(is_anagram(s1,s2))
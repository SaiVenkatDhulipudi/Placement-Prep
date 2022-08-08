#https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
int kthElement(int arr1[], int arr2[], int n, int m, int k)
    {
        map<int,int>mp;
        for(int i=0;i<n;i++)mp[arr1[i]]+=1;
        for(int i=0;i<m;i++)mp[arr2[i]]+=1;
        for(auto i:mp)
        {
            k-=i.second;
            if(k<=0)
            {
                return i.first;
            }
        }
    }

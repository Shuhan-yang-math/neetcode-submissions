class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        A=[]
        a=sorted(nums)
        n=len(a)
        for i in range(n-2):
            if i>0 and a[i]==a[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                if a[i]+a[j]+a[k]==0:
                    A.append([a[i],a[j],a[k]])
                    j=j+1
                    k=k-1
                    while j<k and a[j]==a[j-1]:
                        j=j+1
                    while j<k and a[k]==a[k+1]:
                        k=k-1
                elif a[i]+a[j]+a[k]>0:
                    k=k-1
                else:
                    j=j+1
        return A
        
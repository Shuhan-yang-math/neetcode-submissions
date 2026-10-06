class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums1=num1
        nums2=num2
        if nums1=='0' or nums2=="0":
            return "0"
        m=len(nums1)
        n=len(nums2)
        C=[0]*(m+n)
        for i in range(m):
            for j in range(n):
                C[i+j+1]+=(ord(nums1[i])-ord("0"))*(ord(nums2[j])-ord("0"))       
        for k in range(m+n-1,0,-1):
            C[k-1]+=C[k]//10
            C[k]=C[k]%10
        result="".join(str(d) for d in C).lstrip("0")
        return result
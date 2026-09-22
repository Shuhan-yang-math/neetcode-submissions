class TimeMap:

    def __init__(self):
        self.data={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key]=[]
        self.data[key].append([timestamp,value])        

    def get(self, key: str, timestamp: int) -> str:
        records=self.data.get(key,[])
        i,j=0,len(records)-1
        result=""
        while i<=j:
            k=(i+j)//2
            if records[k][0]<=timestamp:
                result=records[k][1]
                i=k+1
            else:
                j=k-1
        return result








        

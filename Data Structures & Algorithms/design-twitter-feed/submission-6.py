class Twitter:

    def __init__(self):
        self.A=[]
        self.B={}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.A.append([userId,tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result=[]
        for i in reversed(self.A):
            if i[0]==userId or i[0] in self.B.get(userId,set()):
                result.append(i[1])
            if len(result)==10:
                break
        return result

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.B:
            self.B[followerId]=set()
            self.B[followerId].add(followeeId)
        else:
            self.B[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.B[followerId].discard(followeeId)
        

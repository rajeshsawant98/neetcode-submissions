class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -=1
        self.tweetMap[userId].append([self.count,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap= []

        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            if self.tweetMap[followee]:
                index = len(self.tweetMap[followee]) - 1
                count, tweetId = self.tweetMap[followee][index]
                minHeap.append([count,tweetId,followee,index-1])
        heapq.heapify(minHeap)
        
        while minHeap and len(res)<10:
            count,tweetId,followeeId,index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >=0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId,followeeId,index -1])



        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
            


        

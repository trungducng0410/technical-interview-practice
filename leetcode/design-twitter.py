class Twitter:

    def __init__(self):
        self.followers = {}  # {[userId: string]: Set}
        self.tweets = []  # max Heap
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followers:
            self.followers[userId] = {userId}

        heapq.heappush(self.tweets, (-self.time, userId, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tmp = []
        res = []

        # Get 10 most recent tweets
        while len(self.tweets) > 0 and len(res) < 10:
            tweet = heapq.heappop(self.tweets)
            if tweet[1] in self.followers[userId]:
                res.append(tweet[2])
            tmp.append(tweet)

        # Push back tweets to heap
        while tmp:
            tweet = tmp.pop()
            heapq.heappush(self.tweets, tweet)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = {followerId}

        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followMap[userId].add(userId)
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([time, tweetId, followeeId, index - 1])

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

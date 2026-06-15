from heapq import *
class Twitter:

    def __init__(self):
        self.counter = 0
        self.user_followers = defaultdict(set) #key:user, values:ids which user follows
        self.user_tweets = defaultdict(deque) ##size limit:10
       
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter-=1
        self.user_tweets[userId].appendleft((self.counter,tweetId))
        if len(self.user_tweets[userId])>10:
            self.user_tweets[userId].pop()
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        for follower in self.user_followers[userId] | {userId}:
            if len(self.user_tweets[follower]):
                heappush(heap,(self.user_tweets[follower][0][0],self.user_tweets[follower][0][1],0,follower))
                if len(heap)>10:
                    heappop(heap)
        res=[]
        while len(res)<10 and heap:
            time,tweet_id,idx,uid = heappop(heap)
            res.append(tweet_id)
            if idx < len(self.user_tweets[uid])-1:
                idx+=1
                heappush(heap,(self.user_tweets[uid][idx][0],self.user_tweets[uid][idx][1],idx,uid))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
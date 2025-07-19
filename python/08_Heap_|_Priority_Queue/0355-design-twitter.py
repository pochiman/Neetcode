"""

355. Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow 
another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

• Twitter() Initializes your twitter object.

• void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by 
  the user userId. Each call to this function will be made with a unique tweetId.

• List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in 
  the user's news feed. Each item in the news feed must be posted by users who the 
  user followed or by the user themself. Tweets must be ordered from most recent 
  to least recent.

• void follow(int followerId, int followeeId) The user with ID followerId started 
  following the user with ID followeeId.

• void unfollow(int followerId, int followeeId) The user with ID followerId started 
  unfollowing the user with ID followeeId.



Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", 
"unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id 
-> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids 
-> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id 
-> [5], since user 1 is no longer following user 2.

"""

# Solution 2: Heap [✔️]
# Time Complexity: O(n log n) for each getNewsFeed() call and O(1) for remaining methods.
# Space Complexity: O(N * m + N * M + n)

# Where n is the total number of followeeIds associated with the userId, m is the maximum 
# number of tweets by any user, N is the total number of userIds and M is the maximum 
# number of followees for any user.

class Twitter: # type: ignore
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # type: ignore # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # type: ignore # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]: # type: ignore
        res = []  # ordered starting from recent
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap) # type: ignore
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap) # type: ignore
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1]) # type: ignore
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


######## ######## ######## ######## ######## ######## ########


# Solution 3: Heap (Optimal)
# Time Complexity: O(n) for each getNewsFeed() call and O(1) for remaining methods.
# Space Complexity: O(N * m + N * M + n)

# Where n is the total number of followeeIds associated with the userId, m is the maximum 
# number of tweets by any user (m can be at most 10), N is the total number of userIds and 
# M is the maximum number of followees for any user.

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # type: ignore # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # type: ignore # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]: # type: ignore
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        if len(self.followMap[userId]) >= 10:
            maxHeap = []
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1]) # type: ignore
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap) # type: ignore
            while maxHeap:
                count, tweetId, followeeId, index = heapq.heappop(maxHeap) # type: ignore
                heapq.heappush(minHeap, [-count, tweetId, followeeId, index]) # type: ignore
        else:
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1]) # type: ignore

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap) # type: ignore
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1]) # type: ignore
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
"""

981. Time Based Key-Value Store

Design a time-based key-value data structure that can store multiple values for 
the same key at different time stamps and retrieve the key's value at a certain 
timestamp.

Implement the TimeMap class:

• TimeMap() Initializes the object of the data structure.

• void set(String key, String value, int timestamp) Stores the key key with the 
  value value at the given time timestamp.

• String get(String key, int timestamp) Returns a value such that set was called 
  previously, with timestamp_prev <= timestamp. If there are multiple such values, 
  it returns the value associated with the largest timestamp_prev. If there are 
  no values, it returns "".



Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], 
["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with 
timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding 
to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with 
timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

"""

# Solution 3: Binary Search (Array) [✔️]
# Time Complexity: O(1) for set() and O(log n) for get().
# Space Complexity: O(m * n)

# Where n is the total number of values associated with a key 
# and m is the total number of keys.

class TimeMap:

    def __init__(self):
        self.store = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
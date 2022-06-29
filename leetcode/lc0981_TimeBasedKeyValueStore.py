# Design a time-based key-value data structure that can store multiple values
# for the same key at different time stamps and retrieve the key's value at a
# certain timestamp.
# Implement the TimeMap class:
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with
# the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was
# called previously, with timestamp_prev <= timestamp. If there are multiple
# such values, it returns the value associated with the largest timestamp_prev.
# If there are no values, it returns "".
# Constraints:
#   1 <= key.length, value.length <= 100
#   key and value consist of lowercase English letters and digits.
#   1 <= timestamp <= 107
#   All the timestamps timestamp of set are strictly increasing.
#   At most 2 * 105 calls will be made to set and get.
from collections import defaultdict


# Map + List + Binary Search - O(1), O(log(n))
class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.data[key]
        if not values:
            return ""

        i, j = 0, len(values) - 1   # bisect_left
        while i < j:
            k = (i + j) // 2
            if values[k][0] < timestamp:
                i = k + 1
            else:
                j = k

        if values[i][0] <= timestamp:   # be careful about edge condition after bisect_left
            return values[i][1]
        elif i > 0:
            return values[i-1][1]
        else:
            return ""


if __name__ == "__main__":

    def unit_test1(timemap):
        obj = timemap()

        inputs = [["set", "get", "get", "set", "get", "get"],
                  [["foo", "bar", 1], ["foo", 1], ["foo", 3], 
                   ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]]
        expected = [None, "bar", "bar", None, "bar2", "bar2"]
        outputs = []
        for i in range(len(inputs[0])):
            outputs.append(getattr(obj, inputs[0][i])(*inputs[1][i]))
        print(outputs)
        assert outputs == expected

    def unit_test2(timemap):
        obj = timemap()

        inputs = [["set","set","get","get","get","get","get"],
                  [["love","high",10],["love","low",20],["love",5],
                   ["love",10],["love",15],["love",20],["love",25]]]
        expected = [None, None, "","high","high","low","low"]
        outputs = []
        for i in range(len(inputs[0])):
            outputs.append(getattr(obj, inputs[0][i])(*inputs[1][i]))
        print(outputs)
        assert outputs == expected


    unit_test1(TimeMap)
    unit_test2(TimeMap)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

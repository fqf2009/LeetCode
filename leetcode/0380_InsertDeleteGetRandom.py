# Implement the RandomizedSet class:
#  - RandomizedSet() Initializes the RandomizedSet object.
#  - bool insert(int val) Inserts an item val into the set if not present. 
#    Returns True if the item was not present, False otherwise.
#  - bool remove(int val) Removes an item val from the set if present. 
#    Returns True if the item was present, False otherwise.
#  - int getRandom() Returns a random element from the current set of elements
#    (it's guaranteed that at least one element exists when this method is
#    called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works
# in average O(1) time complexity.
# Constraints:
#   -2^31 <= val <= 2^31 - 1
#   At most 2 * 105 calls will be made to insert, remove, and getRandom.
#   There will be at least one element in the data structure when getRandom is called.
import random

# Dict + List
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.idx = []

    def insert(self, val: int) -> bool:
        if val in self.map: return False
        self.map[val] = len(self.idx)
        self.idx.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map: return False
        i = self.map[val]
        if i < len(self.idx) - 1:
            self.map[self.idx[-1]] = i  # update map!!!
            self.idx[i] = self.idx[-1]
        self.idx.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.idx)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == "__main__":
    from unittest import TestCase, main
    from unittest.mock import patch
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(RandomizedSet,)])    # must be tuple!!!
    class TestSolution(TestCase):
        @parameterized.expand([
            (["insert", "insert", "remove", "insert", "remove", "getRandom"], 
             [[0], [1], [0], [2], [1], []], 
             [True, True, True, True, True, 2]),
            (["insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"], 
             [[1], [2], [2], [], [1], [2], []], 
             [True, False, True, 2, True, False, 2]),
        ])
        def test_maximumProduct(self, inputs, params, expected):
            sol = self.solution()   # type:ignore
            outputs = []
            for i in range(len(inputs)):
                r = getattr(sol, inputs[i])(*params[i])
                outputs.append(r)
            assert outputs == expected

    main()

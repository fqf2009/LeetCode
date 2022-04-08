# A Bitset is a data structure that compactly stores bits.
# Implement the Bitset class:
#  - Bitset(int size) Initializes the Bitset with size bits, all of which are 0.
#  - void fix(int idx) Updates the value of the bit at the index idx to 1.
#    If the value was already 1, no change occurs.
#  - void unfix(int idx) Updates the value of the bit at the index idx to 0. 
#    If the value was already 0, no change occurs.
#  - void flip() Flips the values of each bit in the Bitset. In other words,
#    all bits with value 0 will now have value 1 and vice versa.
#  - boolean all() Checks if the value of each bit in the Bitset is 1. Returns 
#    true if it satisfies the condition, false otherwise.
#  - boolean one() Checks if there is at least one bit in the Bitset with 
#    value 1. Returns true if it satisfies the condition, false otherwise.
#  - int count() Returns the total number of bits in the Bitset which have value 1.
#  - String toString() Returns the current composition of the Bitset. Note that in
#    the resultant string, the character at the ith index should coincide with the 
#    value at the ith bit of the Bitset.

# Constraints:
#  - 1 <= size <= 105
#  - 0 <= idx <= size - 1
#  - At most 105 calls will be made in total to fix, unfix, flip, all, one, count, and toString.
#  - At least one call will be made to all, one, count, or toString.
#  - At most 5 calls will be made to toString.

class Bitset:
    def __init__(self, size: int):
        self.capacity = size
        self.bitstr = ['0'] * size
        self.ones = 0
        self.flipped = False

    def _fix(self, idx: int) -> None:
        if self.bitstr[idx] == '0':
            self.bitstr[idx] = '1'
            self.ones += 1

    def fix(self, idx: int) -> None:
        if self.flipped:
            self._unfix(idx)
        else:
            self._fix(idx)

    def _unfix(self, idx: int) -> None:
        if self.bitstr[idx] == '1':
            self.bitstr[idx] = '0'
            self.ones -= 1

    def unfix(self, idx: int) -> None:
        if self.flipped:
            self._fix(idx)
        else:
            self._unfix(idx)
        
    def flip(self) -> None:
        self.flipped = not self.flipped

    def all(self) -> bool:
        if self.flipped:
            return self.ones == 0
        else:
            return self.capacity == self.ones

    def one(self) -> bool:
        if self.flipped:
            return self.ones < self.capacity
        else:
            return self.ones > 0

    def count(self) -> int:
        if self.flipped:
            return self.capacity - self.ones
        else:
            return self.ones

    def toString(self) -> str:
        if self.flipped:
            return ''.join(['1' if x == '0' else '0' for x in self.bitstr])
        else:
            return ''.join(self.bitstr)


if __name__ == "__main__":
    inputs = [ ["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"],
               [[5], [3], [1], [], [], [0], [], [], [0], [], []] ]
    expected = [None, None, None, None, False, None, None, True, None, 2, "01010"]
    outputs = [None]
    obj = globals()[inputs[0][0]](*inputs[1][0])
    for i in range(1, len(inputs[0])):
        outputs.append(getattr(obj, inputs[0][i])(*inputs[1][i]))
    print(outputs)
    assert outputs == expected

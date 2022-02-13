# You are given two non-negative integers num1 and num2.
# In one operation, if num1 >= num2, you must subtract 
# num2 from num1, otherwise subtract num1 from num2.

# For example, if num1 = 5 and num2 = 4, subtract num2 from 
# num1, thus obtaining num1 = 1 and num2 = 4. However, if 
# num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.

# Return the number of operations required to make either 
# num1 = 0 or num2 = 0.

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 < num2:
            num1, num2 = num2, num1

        res = 0
        while num2 != 0:
            q, r = divmod(num1, num2)
            res += q
            num1, num2 = num2, r

        return res


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.countOperations(num1=2, num2=3)
        print(r)
        assert r == 3

        r = sol.countOperations(num1=10, num2=10)
        print(r)
        assert r == 1

    unitTest(Solution())

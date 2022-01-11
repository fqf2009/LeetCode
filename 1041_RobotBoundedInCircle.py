# On an infinite plane, a robot initially stands at (0, 0) and faces north. 
# The robot can receive one of three instructions:
#   "G": go straight 1 unit;
#   "L": turn 90 degrees to the left;
#   "R": turn 90 degrees to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the
# robot never leaves the circle.

# Compute the vector of movement after performing all instructions.
# The robot will be bound in a circle if and only if:
#  - robot returns to origin, or
#  - robot changes its direction
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        move = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        x, y = 0, 0
        for ins in instructions:
            if ins == 'G':
                x += move[direction][0]
                y += move[direction][1]
            elif ins == 'L':
                direction = (direction + 1) % 4
            else:
                direction = (direction + 4 - 1) % 4
        
        return direction != 0 or (x == 0 and y ==0)


if __name__ == '__main__':
    sol = Solution()

    r = sol.isRobotBounded("GGLLGG")
    print(r)
    assert(r == True)

    r = sol.isRobotBounded("GG")
    print(r)
    assert(r == False)

    r = sol.isRobotBounded("GL")
    print(r)
    assert(r == True)

# On a single-threaded CPU, we execute a program containing n functions.
# Each function has a unique ID between 0 and n-1.
# Function calls are stored in a call stack: when a function call starts,
# its ID is pushed onto the stack, and when a function call ends, its ID
# is popped off the stack. The function whose ID is at the top of the
# stack is the current function being executed. Each time a function starts
# or ends, we write a log with the ID, whether it started or ended, and the
# timestamp.
# You are given a list logs, where logs[i] represents the ith log message
# formatted as a string "{function_id}:{"start" | "end"}:{timestamp}".
# For example, "0:start:3" means a function call with function ID 0 started
# at the beginning of timestamp 3, and "1:end:2" means a function call with
# function ID 1 ended at the end of timestamp 2. Note that a function can
# be called multiple times, possibly recursively.
# A function's exclusive time is the sum of execution times for all function
# calls in the program. For example, if a function is called twice, one call
# executing for 2 time units and another call executing for 1 time unit,
# the exclusive time is 2 + 1 = 3.
# Return the exclusive time of each function in an array, where the value
# at the ith index represents the exclusive time for the function with ID i.
# Constraints:
#   1 <= n <= 100
#   1 <= logs.length <= 500
#   0 <= function_id < n
#   0 <= timestamp <= 10^9
#   No two start events will happen at the same timestamp.
#   No two end events will happen at the same timestamp.
#   Each function has an "end" log for each "start" log.
from typing import List


# Stack: T/S: O(n), O(n)
# - wierd problem design: 
#   - a function call started at the beginning of timestamp t
#   - a function call ended at the end of timestamp t
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        task_stack = []
        cpu = [0] * n
        prev_time = 0
        for logline in logs:
            log_arr = logline.split(":")
            func, activity, curr_time = int(log_arr[0]), log_arr[1], int(log_arr[2])
            if activity == "start":
                if task_stack:
                    task = task_stack[-1]
                    cpu[task] += curr_time - prev_time # start time is at the start of t
                prev_time = curr_time
                task_stack.append(int(func))
            else:  # 'stop'
                task = task_stack.pop()
                cpu[task] += curr_time + 1 - prev_time # end time is at the end of t
                prev_time = curr_time + 1

        return cpu


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"])
        print(r)
        assert r == [3, 4]

        r = sol.exclusiveTime(1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"])
        print(r)
        assert r == [8]

        r = sol.exclusiveTime(2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"])
        print(r)
        assert r == [7, 1]

    unit_test(Solution())

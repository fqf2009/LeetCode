# Given a string path, which is an absolute path (starting with a slash '/') to 
# a file or directory in a Unix-style file system, convert it to the simplified 
# canonical path.
# In a Unix-style file system, a period '.' refers to the current directory, a 
# double period '..' refers to the directory up a level, and any multiple 
# consecutive slashes (i.e. '//') are treated as a single slash '/'. For this 
# problem, any other format of periods such as '...' are treated as 
# file/directory names.
# The canonical path should have the following format:
# - The path starts with a single slash '/'.
# - Any two directories are separated by a single slash '/'.
# - The path does not end with a trailing '/'.
# - The path only contains the directories on the path from the root directory 
#   to the target file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path.
# Constraints:
#   1 <= path.length <= 3000
#   path consists of English letters, digits, period '.', slash '/' or '_'.
#   path is a valid absolute Unix path.


# Stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        stack = []
        for i, x in enumerate(arr):
            # '' is due to: before leading '/' or between '//' or after last '/'
            if x == '' and len(stack) > 0 or x == '.':
                continue
            if x == '..':
                if stack and stack[-1] != '':
                    stack.pop()
                continue
            stack.append(x)

        new_path = '/'.join(stack)
        if new_path == '':
            new_path = '/'
        
        return new_path
    

if __name__ == "__main__":
    def unitTest(sol):
        r = sol.simplifyPath('/home/')
        print(r)
        assert(r == '/home')

        r = sol.simplifyPath('/../')
        print(r)
        assert(r == '/')

        r = sol.simplifyPath('/home//foo/')
        print(r)
        assert(r == '/home/foo')

        r = sol.simplifyPath('/a/./b/../../c/')
        print(r)
        assert(r == '/c')

    unitTest(Solution())

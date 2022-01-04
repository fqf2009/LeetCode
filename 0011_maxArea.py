# You are given an integer array height of length n. There are n vertical lines 
# drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the 
# container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

def maxArea(heights):
    start = 0
    end = len(heights) - 1
    area = 0
    while start < end:
        width = end - start
        if heights[start] < heights[end]:
            high = heights[start]
            start +=1
        else:
            high = heights[end]
            end -= 1
        
        area = max(width * high, area)
    
    return area

if __name__ == '__main__':
    a = maxArea([1,8,6,2,5,4,8,3,7])
    print(a); assert(a == 49)
    
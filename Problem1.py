# Problem 1 : Arithmetic Slices
# Time Complexity : 
'''
Brute force - O(n^2) where n is the size of nums list
1-d array dp - O(n) where n is the size of nums list
dp - O(n) where n is the size of nums list
'''
# Space Complexity :
'''
Brute force - O(1)
1-d array dp - O(n) where n is the size of nums list
dp - O(1)
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

# Brute force
from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # get the length of the nums list
        length = len(nums)
        # define the variable count and set to 0
        count = 0

        # loop from 0 to (length-2)
        for i in range(length-2):
            # get the difference between (i+1)th and ith element in the nums
            diff = nums[i+1] - nums[i]
            # loop from (i+2) to length
            for j in range(i+2, length):
                # check if the difference between jth and (j-1)th element and previous calculated diff
                if(nums[j] - nums[j-1] == diff):
                    # if it is equal then increment the count
                    count += 1
                else:
                    # else break the loop
                    break
        # return the count
        return count

# 1-d array
from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # get the length of the nums list
        length = len(nums)
        # define the variable count and set to 0
        count = 0
        # define dp array with the size same as nums list and fill with 0
        dp = [0] * (length)
        # loop from (length-3) to 0
        for i in range(length-3, -1, -1):
            # check if the difference between (i+2)th and (i+1)th element and difference between (i+1)th and ith element are same
            if(nums[i+2] - nums[i+1] == nums[i+1] - nums[i]):
                # if it is same then set the dp value at ith element as sum of 1 and value of (i+1)th element of dp arrray
                dp[i] = dp[i+1] + 1
            else:
                # else set the value of dp as 0
                dp[i] = 0
            # update count by adding the value of ith element as dp to count
            count += dp[i]
        # return the count
        return count


# 3 variables
from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # get the length of the nums list
        length = len(nums)
        # define the variable count and set to 0
        count = 0
        # define variables right to store the values for right element in the list and value for the current element in the list
        right = 0
        current = 0
        # loop from (length-3) to 0
        for i in range(length-3, -1, -1):
            # check if the difference between (i+2)th and (i+1)th element and difference between (i+1)th and ith element are same
            if(nums[i+2] - nums[i+1] == nums[i+1] - nums[i]):
                # if it is same then set the current value as 1 + value of right variable
                current = right + 1
            else:
                # else set the current as 0
                current = 0
            # update the count by adding the value of current to count
            count += current
            # set the right variable to current 
            right = current
        # return the count
        return count

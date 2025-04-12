# Problem 2 : Triangle
# Time Complexity : 
'''
Memoziation - O(n^2) where n is the size of the triangle list
Bottom-up 2-d array - O(n^2) where n is the size of the triangle list
Bottom-up 1-d array - O(n^2) where n is the size of the triangle list
Using input - O(n^2) where n is the size of the triangle list
'''
# Space Complexity :
'''
Memoziation - O(n^2) where n is the size of the triangle list
Bottom-up 2-d array - O(n^2) where n is the size of the triangle list
Bottom-up 1-d array - O(n) where n is the size of the triangle list
Using input - O(1) 
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

# Memoization - 
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # get the length of the triangle list
        length = len(triangle)
        # define memo array with the length equal to triangle list and fill witn '-inf'
        memo = [[float('-inf')] * length for _ in range(length)]
        # return the value returned by helpfer function
        # call helper function with parameter triangle, row 0, column 0 and memo array
        return self.helper(triangle, 0, 0, memo)
    
    # helper function to calculate the minimum path sum for ith row and jth column
    def helper(self, triangle: List[List[int]], i: int, j: int, memo: List[List[int]]) -> int:
        # base case
        # if the value of i is equal to the length of the triangle list then return 0
        if i == len(triangle):
            return 0
        # if the value of memo at ith and jth position is already calculated then return that value
        if memo[i][j] != float('-inf'):
            return memo[i][j]
        
        # case1 is the value for the new row and jth column
        case1 = self.helper(triangle, i+1, j, memo)
        # case1 is the value for the new row and j+1th column
        case2 = self.helper(triangle, i+1, j+1, memo)
        # calculate the value as sum of value of triangle list at ith and jth position and minimum value between case1 and case2
        result = min(case1, case2) + triangle[i][j]
        # store result in the memo matrix at ith and jth position
        memo[i][j] = result
        # return result
        return result

# bottom-up 2-d array
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # get the length of the triangle list
        length = len(triangle)
        # define dp matrix with size as (length of triangle * length of triangle) and fill with 0
        dp = [[0] * length for _ in range(length)]
        # loop from 0 to length
        for j in range(length):
            # set the value of last row with the value of triangle of last row
            dp[length-1][j] = triangle[length-1][j]
        
        # loop from length-2 to 0
        for i in range(length-2, -1, -1):
            # loop from 0 to i+1
            for j in range(i+1):
                # set the value of dp at ith and jth position as sum of minimum value of dp at (i+1)th jth position and (i+1)th (j+1)th position and value of triangle list at ith and jth position
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        # return value at 0th row and 0th column
        return dp[0][0]


# bottom-up 1-d array
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # get the length of the triangle list
        length = len(triangle)
        # define dp array with size as (length of triangle) and fill with 0
        dp = [0] * (length)
        # loop from 0 to length
        for j in range(length):
            # set the value of last row with the value of triangle of last row
            dp[j] = triangle[length-1][j]
        
        # loop from length-2 to 0
        for i in range(length-2, -1, -1):
            # loop from 0 to i+1
            for j in range(i+1):
                # set the value of dp at jth position as sum of minimum value of dp at jth position and (j+1)th position and value of triangle list at ith and jth position
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        # return value at 0th position
        return dp[0]

# Using triangle list
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # get the length of the triangle list
        length = len(triangle)
        
        # loop from length-2 to 0
        for i in range(length-2, -1, -1):
            # loop from 0 to i+1
            for j in range(i+1):
                # calculate the result as sum of minimum value of triangle list at (i+1)th and jth position and value of triangle list at (i+1)th and (j+1)th position and value of triangle list at ith and jth position
                result = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
                # store the result in the ith and jth position
                triangle[i][j] = result
        # return the value of 0th row and 0th column
        return triangle[0][0]

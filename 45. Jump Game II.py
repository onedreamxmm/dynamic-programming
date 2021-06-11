'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000
'''

class Solution:
    def jump(self, nums):  # DP
        n = len(nums)
        nJumps = [0] * n
        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                nJumps[i] = float('inf')
            else:
                nJumps[i] = 1 + min(nJumps[i+1:i+nums[i]+1])
        return nJumps[0]

    def jump(self, nums: List[int]) -> int:  # preferable solution
        l = r = 0
        nJumps = 0
        while r < len(nums) - 1:
            nJumps += 1
            furthest = max([i + nums[i] for i in range(l, r + 1)])
            l, r = r + 1, furthest

        return nJumps

        # Time complexity: O(N)
        # Space complexity: O(1)






'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105

Complexity Analysis
Time complexity : O(n). We are doing a single pass through the nums array, hence nn steps, where nn is the length of array nums.
Space complexity : O(1). We are not using any extra memory.
'''

class Solution:
    def canJump1(self, nums):
        n = len(nums)
        target = n -1
        for i in range(n - 2, -1, -1):  # Iterate backwards from second to last item until the first item
            if i + nums[i] >= target:    # If this index has jump count which can reach to or beyond the last position
                target = i   # Since we just need to reach to this new index
        return target == 0

    def canJump2(self, nums):  # Going forwards. m represents the maximum index we can reach so far.
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True

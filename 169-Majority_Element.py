# link - https://leetcode.com/problems/majority-element/description/

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


from collections import Counter

def majorityElement(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    # solution 1
    count, res = 0, 0
    for i in nums:
        if count == 0:
            res = i
        count += 1 if i == res else -1
    return res

    # O(n) time and O(1) space

    # solution 2
    # creating a frequency counter and returning when result found
    # count = {}
    # for i in nums:
    #     count[i]= count.get(i,0) + 1
    #     if count[i] > len(nums) // 2:
    #         return i

    # O(n) time and O(m) space for both solutions

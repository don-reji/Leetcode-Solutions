# link - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

"""Given an array nums of n integers where nums[i] is in the range [1, n], return an array
of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # solution 1 O(n) space and time
        set_nums = set(nums)
        result = []
        for i in range(1, n + 1):
            if i not in set_nums:
                result.append(i)
        return result

        # solution 2 O(n) time and O(1) space
        # for num in nums:
        #     index=abs(num)-1

        #     nums[index]=-abs(nums[index])

        # missing_numbers=[ i+1 for i in range(n) if nums[i]>0 ]
        # return missing_numbers

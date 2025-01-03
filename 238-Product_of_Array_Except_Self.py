# link - https://leetcode.com/problems/product-of-array-except-self/description/
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the 
product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does 
not count as extra space for space complexity analysis.)
"""

def productExceptSelf(self, nums: List[int]) -> List[int]:
    n=len(nums)
    res=[1]*n
    con=1
    
    """ 
    calculate the prefix product for each element 
    (i.e., product of all elements to the left of the current index).
    """
    for i in range(1,n):
        res[i]=res[i-1]*nums[i-1]

    '''
    calculate the suffix product for each element 
    (i.e., product of all elements to the right of the current index).
    Update the `res` array by multiplying with the current suffix product, 
    which is tracked using the variable `con`
    '''
    for j in range(1,n+1):
        res[-j]*=con
        con*=nums[-j]
    return res

# Time complexity: O(n) Space complexity: O(1) excluding the output array
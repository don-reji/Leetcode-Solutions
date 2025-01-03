# link - https://leetcode.com/problems/third-maximum-number/

""" Given an integer array nums, return the third distinct maximum number in this array. If the third 
 maximum does not exist, return the maximum number.

 Example 1:

 Input: nums = [3,2,1]
 Output: 1
 Explanation:
 The first distinct maximum is 3.
 The second distinct maximum is 2.
 The third distinct maximum is 1.
 Example 2:

 Input: nums = [1,2]
 Output: 2
 Explanation:
 The first distinct maximum is 2.
 The second distinct maximum is 1.
 The third distinct maximum does not exist, so the maximum (2) is returned instead.
 Example 3:

 Input: nums = [2,2,3,1]
 Output: 1
 Explanation:
 The first distinct maximum is 3.
 The second distinct maximum is 2 (both 2's are counted together since they have the same value).
 The third distinct maximum is 1.
"""


def thirdMax(self, nums: List[int]) -> int:       

# solution 1

    first= second = third= -inf
    
    for i in nums:
        if i in [first,second ,third]:
            continue
        
        if i>first:
            first,second,third=i,first,second
        elif i>second:
            second,third=i,second
        elif i>third:
            third=i
        
    return third if third!=-inf else first
#     O(n) time and O(1) space

    
#         solution 2

#         distinct=list(set(nums))
    
#         if len(distinct)<3:
#             return max(distinct)
    
#         for i in range(2):
#             distinct.remove(max(distinct))
#         return max(distinct)

#     O(n) space and time
# copy nums into set,then list. remove the 1 and 2 largest values, then only 3 largest left. 
# return the max number
    
#     solution 3

    # distinct.sort()
    # return distinct[-3]
#     O(nlogn) time and O(n) space
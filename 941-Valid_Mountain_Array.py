# link - https://leetcode.com/problems/valid-mountain-array/description/
"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 
Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""

def validMountainArray(self, arr: List[int]) -> bool:       
    n = len(arr)
    
    if n < 3:  # Mountain array must have at least 3 elements
        return False

    i, j = 0, n - 1

    # Climb up the left side
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    # Climb down the right side
    while j > 0 and arr[j] < arr[j - 1]:
        j -= 1

    # The peak must be the same for both `i` and `j`
    return i == j and i != 0 and j != n - 1

    # O(n) time complexity and O(1) space complexity
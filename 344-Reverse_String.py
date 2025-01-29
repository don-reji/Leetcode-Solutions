# link - https://leetcode.com/problems/reverse-string/description/
"""
Write a function that reverses a string. The input string is given as an array of 
characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n = len(s)
    for i in range(n//2):
        s[i],s[n-i-1] = s[n-i-1], s[i]

# O(n) time and O(1) space
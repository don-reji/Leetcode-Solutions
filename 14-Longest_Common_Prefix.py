# link - https://leetcode.com/problems/longest-common-prefix/
""" Write a function to find the longest common prefix string amongst an array of strings.

 If there is no common prefix, return an empty string "".

 Example 1:

 Input: strs = ["flower","flow","flight"]
 Output: "fl"
 Example 2:

 Input: strs = ["dog","racecar","car"]
 Output: ""
 Explanation: There is no common prefix among the input strings.

 Constraints:

 1 <= strs.length <= 200
 0 <= strs[i].length <= 200
 strs[i] consists of only lowercase English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        start = strs[0]
        for i in range(len(start)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or start[i] != strs[j][i]:
                    return start[:i]
        return start


# O(n) time and O(1) space

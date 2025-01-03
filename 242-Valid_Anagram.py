# link - https://leetcode.com/problems/valid-anagram/description/

""" Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 An Anagram is a word or phrase formed by rearranging the letters of a different word
 or phrase, typically using all the original letters exactly once.

 Example 1:

 Input: s = "anagram", t = "nagaram"
 Output: true
 Example 2:

 Input: s = "rat", t = "car"
 Output: false

 Constraints:

 1 <= s.length, t.length <= 5 * 104
 s and t consist of lowercase English letters."""


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # solution 1
        return Counter(s) == Counter(t)

        # solution 2
        # count_t,count_s={},{}
        # for i in range(len(s)):
        #     count_s[s[i]]=1+count_s.get(s[i],0)
        #     count_t[t[i]]=1+count_t.get(t[i],0)
        # return count_s==count_t

    # O(n) time and space

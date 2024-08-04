# link- https://leetcode.com/problems/group-anagrams/description/
# Given an array of strings strs, group the anagrams together. You can return the answer in
# any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # if len < 2, no words to anagram
        if len(strs) < 2:
            return [strs]

        result = defaultdict(list)

        for word in strs:
            count =[0]*26

            for char in word:
                count[ord(char)-ord('a')] +=1

            result[tuple(count)].append(word)

        return result.values()
    # O(mn) time and space
    
        # sol 2
        for word in strs:
            result["".join(sorted(word))].append(word)

        return result.values()

        # O(n * mlogm) time , O(mn) space

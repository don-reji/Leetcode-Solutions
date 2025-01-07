# link - https://leetcode.com/problems/jewels-and-stones/description/
"""
You're given strings jewels representing the types of stones that are jewels, and stones 
representing the stones you have. Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 
Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""

def numJewelsInStones(self, jewels: str, stones: str) -> int:
    # storing count of each stone into a dictionary
    count = {}
    for i in stones:
        if i not in count:
            count[i] = 1
            continue
        count[i]+=1

    res=0
    # adding the sum of all the jewels in stones
    for j in jewels:
        res+= count.get(j,0)
    return res

# O(n) time and space
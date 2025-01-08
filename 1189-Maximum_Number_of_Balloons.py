# link - https://leetcode.com/problems/maximum-number-of-balloons/description/
""""
Given a string text, you want to use the characters of text to form as many instances 
of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances 
that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1
Example 2:

Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 
Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""

def maxNumberOfBalloons(self, text: str) -> int:
    res = len(text)
    
    balloon = {
        'b'  ,
        'a'  ,
        'l'  ,
        'o'  , 
        'n' 
    }

    # frequency of each character in text
    count = {}
    for i in text:
        if i not in count:
            count[i] = 1
            continue
        count[i]+=1
    """
    Adjust for Repeated Letters in "balloon"
    In the word "balloon," the letters 'l' and 'o' appear twice..
    The get() method ensures that if 'l' or 'o' is not in count, it defaults 
    to 0 to avoid errors.
    """
    count['o'] = count.get('o',0) // 2
    count['l'] = count.get('l',0) // 2


    # find minimum frequency
    for i in balloon:
        res = min(res,count.get(i,0))
    return res

# O(n) time and O(1) space
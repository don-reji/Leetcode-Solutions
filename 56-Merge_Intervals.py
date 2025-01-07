# link - https://leetcode.com/problems/merge-intervals/description/
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""



def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # return intervals back if only 1
    n = len(intervals)
    if n == 1:
        return intervals

    intervals.sort()

    # adding the first interval to result
    res = [intervals[0]]

    for i in range(1, n):
        # checking if start of this interval <= previous entry in result,
        # which means there is an overlap
        if intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(intervals[i][1], res[-1][1])

        # else add interval to result
        else:
            res.append(intervals[i])

    return res

    # time complexity - O(nlogn)
    # space complexity - O(n)

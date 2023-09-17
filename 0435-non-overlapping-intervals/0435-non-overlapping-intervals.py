class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort the intervals by their end points in ascending order
        intervals.sort(key=lambda x: x[1])
        
        prev = intervals[0]
        cnt = 0
        
        for a in intervals[1:]:
            if a[0] < prev[1]:
                # Overlapping interval found
                cnt += 1
            else:
                # Non-overlapping interval, update prev
                prev = a
        
        return cnt


        return cnt

        
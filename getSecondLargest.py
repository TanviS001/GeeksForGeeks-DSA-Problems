class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1
        
        unique_sorted_arr = sorted(set(arr), reverse=True)
        
        if len(unique_sorted_arr) < 2:
            return -1
        
        return unique_sorted_arr[1]

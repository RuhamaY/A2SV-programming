class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def flip(sub_arr, k):
            sub_arr[:k] = sub_arr[:k][::-1]

        res = []
        for size in range(len(arr), 1, -1):
            max_index = arr.index(max(arr[:size]))
            if max_index != size - 1:
                if max_index != 0:
                    flip(arr, max_index + 1)
                    res.append(max_index + 1)
                flip(arr, size)
                res.append(size)
        return res

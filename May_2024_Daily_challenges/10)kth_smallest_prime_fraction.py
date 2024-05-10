class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        arr2 = list()
        needed_dict = {}
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                ans = arr[i]/arr[j]
                arr2.append(ans)
                needed_dict[arr[i], arr[j]] = ans
        needed_arr = sorted(arr2)
        smallest_kth_fraction = needed_arr[k-1]

        for k, v in needed_dict.items():
            if v == smallest_kth_fraction:
                return list(k)
        


sol_obj = Solution()
print(sol_obj.kthSmallestPrimeFraction([1,7], 1))
class solution():
      def maxOddBinaryNumber(self, s):
        arr = sorted(s)
        second_last = len(arr) - 2

        for i in range(len(arr) // 2):
            arr[i], arr[second_last - i] = arr[second_last - i], arr[i]

        return "".join(arr)
      
sol_obj = solution()
print(sol_obj.maxOddBinaryNumber("010"))
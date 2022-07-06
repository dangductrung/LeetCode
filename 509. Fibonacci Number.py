class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        data = [0, 1]
        count = 2
        while count <= n:
            data[count % 2] = data[0] + data[1]
            count += 1
        return max(data)

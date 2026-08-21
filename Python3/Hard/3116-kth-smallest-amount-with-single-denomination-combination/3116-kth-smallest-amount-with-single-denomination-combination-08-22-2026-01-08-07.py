class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
    
        A = []
        for x in coins:
            if all(x % c for c in A):
                A.append(x)
    
        def check(m):
            tot = 0
            for x in range(1, len(A) + 1):
                for c in combinations(A, x):
                    tot += m // lcm(*c) * pow(-1, x + 1)
            return tot >= k
    
        return bisect_left(range(k * A[0] + 1), True, lo=1, key=check)
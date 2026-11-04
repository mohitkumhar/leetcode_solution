class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)
        idx = {v: i + 1 for i, v in enumerate(vals)}
        rk = [idx[v] for v in nums]

        bc = [0] * (m + 1)
        bs = [0] * (m + 1)
        cnt_at = [0] * (m + 1)
        LOG = m.bit_length()
        need = (x + 1) // 2

        def upd(i, c, v):
            while i <= m:
                bc[i] += c
                bs[i] += v
                i += i & -i

        tot = 0
        for i in range(x):
            upd(rk[i], 1, nums[i])
            cnt_at[rk[i]] += 1
            tot += nums[i]

        cost = [0] * (n - x + 1)
        for s in range(n - x + 1):
            pos, kk, acc_c, acc_s = 0, need, 0, 0
            for b in range(LOG, -1, -1):
                np_ = pos + (1 << b)
                if np_ <= m and bc[np_] < kk:
                    pos = np_
                    kk -= bc[np_]
                    acc_c += bc[np_]
                    acc_s += bs[np_]
            p = pos + 1
            med = vals[p - 1]
            cnt_le = acc_c + cnt_at[p]
            sum_le = acc_s + cnt_at[p] * med
            cost[s] = med * cnt_le - sum_le + (tot - sum_le) - med * (x - cnt_le)

            upd(rk[s], -1, -nums[s])
            cnt_at[rk[s]] -= 1
            tot -= nums[s]
            if s + x < n:
                upd(rk[s + x], 1, nums[s + x])
                cnt_at[rk[s + x]] += 1
                tot += nums[s + x]

        INF = float('inf')
        prev = [0] * (n + 1)
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]
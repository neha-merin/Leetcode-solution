from math import gcd


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, l, r, idx, val):
        if l == r:
            self.tree[node] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(node * 2, l, mid, idx, val)
        else:
            self.update(node * 2 + 1, mid + 1, r, idx, val)

        self.tree[node] = gcd(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def query(self, node, l, r, ql, qr):
        if ql > qr:
            return 0

        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l + r) // 2

        if qr <= mid:
            return self.query(node * 2, l, mid, ql, qr)

        if ql > mid:
            return self.query(node * 2 + 1, mid + 1, r, ql, qr)

        return gcd(
            self.query(node * 2, l, mid, ql, mid),
            self.query(node * 2 + 1, mid + 1, r, mid + 1, qr)
        )


class Solution:
    def countGoodSubseq(self, nums: List[int], p: int,
                        queries: List[List[int]]) -> int:

        n = len(nums)
        seg = SegmentTree(n)

        cnt = 0

        # Build initial tree
        for i, x in enumerate(nums):
            if x % p == 0:
                seg.update(1, 0, n - 1, i, x)
                cnt += 1

        ans = 0

        for idx, val in queries:

            # Remove old value's contribution
            if nums[idx] % p == 0:
                seg.update(1, 0, n - 1, idx, 0)
                cnt -= 1

            # Add new value's contribution
            if val % p == 0:
                seg.update(1, 0, n - 1, idx, val)
                cnt += 1

            nums[idx] = val

            # GCD of all elements divisible by p
            if seg.tree[1] != p:
                continue

            # We can exclude all non-divisible elements
            if cnt < n:
                ans += 1
                continue

            # Mathematical shortcut
            if n > 6:
                ans += 1
                continue

            # n <= 6: try removing one element
            for i in range(n):
                left = seg.query(1, 0, n - 1, 0, i - 1)
                right = seg.query(1, 0, n - 1, i + 1, n - 1)

                if gcd(left, right) == p:
                    ans += 1
                    break

        return ans
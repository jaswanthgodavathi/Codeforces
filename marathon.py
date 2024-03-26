class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (2 * n)

    def update(self, idx, start, end, pos):
        if start == end:
            self.tree[idx] = 1
        else:
            mid = (start + end) // 2
            if pos <= mid:
                self.update(2 * idx, start, mid, pos)
            else:
                self.update(2 * idx + 1, mid + 1, end, pos)
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def query(self, idx, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[idx]
        mid = (start + end) // 2
        return self.query(2 * idx, start, mid, left, right) + self.query(2 * idx + 1, mid + 1, end, left, right)


def stockSpike(prices, k):
    n = len(prices)
    count = 0
    seg_tree = SegmentTree(n)

    for i in range(n - 1, -1, -1):
        right_count = seg_tree.query(1, 0, n - 1, i + 1, n - 1)
        if right_count >= k:
            left_count = seg_tree.query(1, 0, n - 1, 0, i - 1)
            if left_count >= k:
                count += 1
        seg_tree.update(1, 0, n - 1, i)

    return count


# Example usage
prices = [1, 3, 2, 5, 4]
k = 1
result = stockSpike(prices, k)
print(result)

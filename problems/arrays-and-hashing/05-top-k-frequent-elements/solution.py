import heapq


def top_k_frequent_sorting(nums: list[int], k: int) -> list[int]:
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    sorted_freq = sorted(freq.items(), key=lambda f: f[1], reverse=True)
    return [item[0] for item in sorted_freq[:k]]


def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for _, num in heap]


print(top_k_frequent_heap(nums=[1, 2, 2, 3, 3, 3], k=2))

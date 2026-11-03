class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        result = []

        for val, frequency in cnt.most_common(k):
            result.append(val)

        return result


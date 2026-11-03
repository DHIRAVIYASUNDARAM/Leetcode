class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums).most_common(k)
        ans=[]
        for val in freq:
            ans.append(val[0])
        return ans

        # cnt = Counter(nums)
        # result = []

        # for val, frequency in cnt.most_common(k):
        #     result.append(val)

        # return result



# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         cnt = Counter(nums)
#         return [val for val, freq in cnt.most_common(k)]

# import heapq

# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         freq = {}

#         for num in nums:
#             freq[num] = freq.get(num, 0) + 1

#         pq = []

#         for num, count in freq.items():

#             if len(pq) < k:
#                 heapq.heappush(pq, (count, num))
#             else:
#                 heapq.heappush(pq, (count, num))
#                 heapq.heappop(pq)

#         result = []

#         while pq:
#             result.append(heapq.heappop(pq)[1])

#         return result






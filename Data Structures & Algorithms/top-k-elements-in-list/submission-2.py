class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, freq in count.items():
            #key value pair will return
            bucket[freq].append(num)

        result = [] #return top k elements
        for i in range(len(bucket) -1, 0, -1): # return in descending order as top k
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result



        
            
        
        
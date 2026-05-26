class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        flipped = dict()

        for i in range(len(nums)):
            opp = target - nums[i]
            if opp in seen.values():
                for key, value in seen.items():
                    flipped[value] = key
                return sorted([i, flipped[opp]])
            else:
                seen[i] = nums[i]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        output: List[int] = []
        for i in range(len(nums)):
            value = nums[i]
            if value not in output:
                output.append(value)
        
        # Write back into nums (in-place)
        nums[:len(output)] = output
        
        return len(output)
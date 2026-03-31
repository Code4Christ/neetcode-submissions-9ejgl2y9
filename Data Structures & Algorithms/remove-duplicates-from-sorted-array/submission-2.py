class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)
        # output = []
        # for i in range(len(nums)):
        #     value = nums[i]
        #     print(f"i is {i} element and {value} value in {nums}")
        #     if value not in output:
        #         output.append(value)
        #     print(f"len of output is {len(output)}, output looks like {output}")
        # answer = len(output)
        
        # return int(len(output))
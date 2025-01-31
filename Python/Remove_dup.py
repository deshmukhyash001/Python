class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        unique_index = 0

        for i in range(1,len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]
        return unique_index + 1

li1 = [1,2,5,4,4,7,8,8]
obj1 = Solution()
hi = obj1.removeDuplicates(li1)
print(li1[:hi])
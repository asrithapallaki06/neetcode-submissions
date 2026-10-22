class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #initialize k
        # for loop i thru the no of elements
        # check if they're not equal to val
            #copy whats not equal to spot with val
            #increment k
        # return k

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

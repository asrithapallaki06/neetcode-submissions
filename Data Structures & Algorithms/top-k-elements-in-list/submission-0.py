class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count the frequency
        frequent = {}
        for num in nums:
            if num in frequent:
                frequent[num] = frequent[num] + 1
            else:
                frequent[num] = 1

        # go thru the shelves and make space for everything
        shelves = []
        for i in range(len(nums) + 1):
            shelves.append([])
        
        # now append each shelf with a number
        for num in frequent:
            count = frequent[num]
            shelves[count].append(num)
        
        #walk shelves from top to bottom
        result = []
        for count in range(len(shelves) -1 , 0, -1):
            for num in shelves[count]:
                result.append(num)
                if(len(result) == k):
                    return result

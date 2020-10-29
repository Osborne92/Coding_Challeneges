class Running_Sum:
    def runningSum(self, nums):
        
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums

class Candy:
    def kidsWithCandies(self, candies, extraCandies):
        
        candy_list = []
        max_candy = max(candies)
        
        for i in candies:
            if i + extraCandies >= max_candy: 
                candy_list.append(True)
            else: 
                candy_list.append(False)
        return candy_list

class Shuffle:
    def shuffle(self, nums, n):
        
        nums_list = []
        first_half = nums[:len(nums)//2]
        second_half = nums[len(nums)//2:]
        
        for (f, s) in zip(first_half, second_half):
            nums_list.append(f)
            nums_list.append(s)
        return nums_list

class Defanged_IP:
    def defangIPaddr(self, address):
        return address.replace('.', '[.]')
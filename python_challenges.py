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

class Pairs:
    def numIdenticalPairs(self, nums):
        n = len(nums)
        pairs = 0
        for i in range(n - 1): # n-1 is neccesary for i to stop one number behind j iterator  
            for j in range(i + 1, n): # i + 1 is used to start iterating one number after i
                if nums[i] == nums[j]:
                    pairs += 1
        return pairs

class Jewels:
    def numJewelsInStones(self, J, S):
        Count = 0
        for s in S:
                if s in J:
                    Count += 1
        return Count

class Reduce_to_Zero:
    def numberOfSteps (self, num):
        count_of_steps = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
            # number is odd...
                num -= 1
            count_of_steps += 1
        return count_of_steps
        

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if nums:
            slow = 0
            for fast in range(1, len(nums)):
                if nums[fast] != nums[slow]:
                    slow += 1
                    nums[slow] = nums[fast]
            return slow + 1
        else:
            return 0
if __name__ == "__main__":
    a=Solution()
    print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))





#!/usr/bin/env python
#283. Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        while (j<len(nums) and i<len(nums)) :
            while (i<len(nums) and nums[i]!=0) : i=i+1
            if i>=len(nums) :return
            print "i=%d,j=%d" %(i,j)
            print nums
            while (j<len(nums) and nums[j]==0): j=j+1
            if j>=len(nums) or j<=i:return
            nums[i]=nums[j]
            nums[j]=0

def main():
    s=Solution()
    nums=[1,0,1]
    s.moveZeroes(nums)
    print nums

if __name__ == "__main__":
    main()

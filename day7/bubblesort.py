def sort(nums):
    sc=0
    for i in range(len(nums)-1,0,-1):# from i value 4 to 0 decrease by 1 each time
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                sc+=1
    return sc,nums
nums=[5,4,3,2,1]
print(sort(nums))
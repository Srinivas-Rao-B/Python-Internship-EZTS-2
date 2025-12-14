def sort(nums):
    s=0
    for i in range(len(nums)):
        min=i
        for j in range(i,len(nums)):
            if nums[j]<nums[min]:
                min=j
        if min!=i:
            temp=nums[i]
            nums[i]=nums[min]
            nums[min]=temp
            s+=1
    return s,nums
nums=[5,4,3,2,1]
print(sort(nums))
        
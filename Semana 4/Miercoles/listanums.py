def count(nums):
     res=[0 for _ in range(len(nums))]
     for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                res[i]+=1
        return res


def main():
    nums=[8,1,2,2,3]
    print(count(nums))

main()
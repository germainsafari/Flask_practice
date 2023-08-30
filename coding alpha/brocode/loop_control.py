# nums = [2,7,11,15]
# target = 6
# hash = {}
# for (i) in range(nums):
#     for j in range(len(nums)):
#         hash.append(i, j)
#         print(hash)
# nums = [2, 7, 11, 15]

# hash = {}
# for i in range(len(nums)):
#     hash[i] = nums[i]
    
    

#     for i in range(len(nums)):
#         if nums[i] in hash:
#             return [hash[nums[i]], i]
#         else:
#             hash[target - nums[i]] = i

# print(hash)
# n = 8
# for i in range(2, n):
#     if n % i == 0:
#         print("not prime")
#     else:
#         print("prime")
    # if n % n == 0 and n % 1 == 0:
    #     print("it is prime")
    
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print("not prime")
#             break
#     else:
#         print("prime")
# else:
#     print("not p")            
# x = [[1,2,3], [3,4,2],[2,6,4]]
# y = [[1,2,3,4],[2,4,5,6],[6,6,5,2]]

# for i in range(len(x)):
#     for i in range(len())
target = 9
nums = [2, 7, 11, 15]
Output = [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
def two_sums(nums, target):
    hash = {}
    for i in range(len(nums)):
        if nums in hash:
            nums[i] += 1
        else:
            nums[i] = 1
    return target
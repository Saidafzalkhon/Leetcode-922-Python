nums = list(map(int,input().split()))
a = list()
b = list()
for i in nums:
    if i%2 == 0 :
               a.append(i)
    else:
               b.append(i)
son = 0
for i in range(len(a)):
    nums[son] = a[i]
    son+=2
son = 1
for i in range(len(b)):
    nums[son] = b[i]
    son+=2
print(nums)
                
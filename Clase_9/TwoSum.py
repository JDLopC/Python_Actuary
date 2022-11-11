def sol1(nums:list, target:int):
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if i == j: continue
            resultado = num1 + num2
            if resultado == target:
                return [i,j]

def sol2(nums:list, target:int):
    for i, num1 in enumerate(nums):
        diff = target- num1
        if diff in nums:
            index = nums.index(diff)
            if index != i:
                return [i, index]

def sol3(nums:list, target:int):
    # Hash map solution
    guia = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in guia:
            return [guia[diff], i]
        guia[num] = i



nums1 = [2, 3, 5, 7, 12, 16]

t11 = 8 #  regresar [1,2]
t12 = 18 # Debería regresar [0,5]

nums2 = [3, 3]
t21 = 6 # [0,1]

nums3 = [5, 5]
t31 = 10 # [0,1]

print(sol3(nums1, t11))
print(sol3(nums1, t12))
print(sol3(nums2, t21))
print(sol3(nums3, t31))
arr1=[2,3,7,5,4]
print(arr1)
print(len(arr1))
print(arr1[0])
print(arr1[1])
print(arr1[-1])
print(arr1[-2])
print(arr1[len(arr1)-1])
print(arr1[len(arr1)//2])

for x in range(len(arr1)):
    print(arr1[x], end=" ")
print()
for x in range(len(arr1)//2+1):
    print(arr1[x], end=" ")


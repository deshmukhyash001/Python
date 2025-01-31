#Searching algorithms

#Linear Search

def Linear_Search(list1, target):
    n = len(list1) 
    for i in range(n):
        if list1[i] == target :
            return i
    return -1
    
list1 = [1,5,8,3,6,2,7]
target = 6
LinearSearch = Linear_Search(list1, target)
if LinearSearch != -1:
    print("Element found at index: ",LinearSearch)
else:
    print("Element not found")

#Binary Search

def Binary_Search(list2,target):
    list2.sort()
    print(list2)
    n = len(list2)
    left = 0
    right = n - 1
    while left <= right :
        mid = (left + right) // 2
        if list2[mid] == target:
            return mid
        elif list2[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

list2 = [1,5,8,2,6,9,3]
target = 1
BinarySearch = Binary_Search(list2,target)
if BinarySearch != -1:
    print("Element found at index: ",BinarySearch)
else:
    print("Element not found")
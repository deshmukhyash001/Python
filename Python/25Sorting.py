#Sorting techniques

#Bubble Sort

def Bubble_sort(list1):
    n = len(list1)
    for i in range(n):
        for j in range(n-i-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return list1

li1 = [1,5,4,7,6]
bs = Bubble_sort(li1)
print(bs)

#Insertion Sort

def Insertion_sort(list2):  
    n = len(list2)
    for i in range(1,n):
        key = list2[i]
        j = i - 1
        while j >= 0 and list2[j] > key:
            list2[j+1] = list2[j]
            j = j - 1
        list2[j+1] = key
    return list2

li2 = [9,8,7,6,5,4,3,2,1]
Insertion = Insertion_sort(li2)
print(Insertion)
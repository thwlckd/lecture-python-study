# MySortings.py

# O(n^2)
def selectionSort(L):
    for i in range(len(L)-1):
        min_index = i
        min = L[min_index]
        for j in range(i+1, len(L)):
            if L[j] < min:
                min_index = j
                min = L[min_index]
        L[i], L[min_index] = L[min_index], L[i]
    return L

def mergeSort(L):
    if len(L) < 2:
        return L

    mid = len(L) // 2
    left_L = mergeSort(L[:mid])
    right_L = mergeSort(L[mid:])

    merged_L = L
    merged_L.clear()
    left = right = 0
    while left < len(left_L) and right < len(right_L):
        if left_L[left] < right_L[right]:
            merged_L.append(left_L[left])
            left += 1
        else:
            merged_L.append(right_L[right])
            right += 1
    merged_L += left_L[left:]
    merged_L += right_L[right:]
    return merged_L

# O(NlogN)  / 정렬이 거의 되어 있는 배열에서 느림 O(N^2)
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

def quick_sort_v2(array):
    if len(array)<=1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# O(N^2)  / 정렬이 거의 되어 있는 배열에서 퀵정렬 보다 빠름
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return array

# O(N+K)  /  최대 값을 알 때, 중복 값이 많을 때, min-max 차이가 작을 때 빠름
def count_sort(array):
    L = [0] * (max(array) + 1)
    for i in array:
        L[i] += 1

    array.clear()
    for i in range(len(L)):
        for _ in range(L[i]):
            array.append(i)

    return array
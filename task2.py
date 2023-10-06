from random import randint, seed

def arr_sort(arr):
    swap = True
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
            if not swap:
                return arr


def search_num(arr, numb, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    if arr[mid] == numb:
        return f"Елемент {numb} має індекс {mid}."
    elif numb < arr[mid]:
        return search_num(arr, numb, left, mid - 1)
    else:
        return search_num(arr, numb, mid + 1, right)


seed(6)
lst = [randint(1, 21) for i in range(20)]
num = int(input("Пошук числа: "))
arr_sort(lst)
s = search_num(lst, num, 0, len(lst) - 1)

print(lst)
print(s)

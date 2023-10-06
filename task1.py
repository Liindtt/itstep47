from random import randint, seed

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)
    merged_list = merge(left, right)
    return merged_list


seed(4)
lst = [randint(1, 20) for i in range(15)]

while True:
    choice = int(input("""\nЯким способом бажаєте відсортувати список?
    1) рекурсивним;
    2) нерекурсивним;
    0) вихід;
>>> """))
    if choice == 1:
        lst_sorted = merge_sort(lst)
        print(lst_sorted)
    elif choice == 2:
        sublist_size = 1
        while sublist_size < len(lst):
            print(f"{sublist_size = }")
            left, mid, right = 0, sublist_size, 2 * sublist_size
            while mid < len(lst):
                print(left, mid, right, end=": ")
                print(lst[left:mid], lst[mid:right])
                lst[left:right] = merge(lst[left:mid], lst[mid:right])
                left, mid, right = left + 2 * sublist_size, mid + 2 * sublist_size, right + 2 * sublist_size
            sublist_size *= 2
            print()
        print(lst)
    elif choice == 0:
        break
    else:
        print("Спробуйте ще раз!")

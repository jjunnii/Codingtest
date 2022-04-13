def inserting_sort(sorting_list):
    for i in range(1, len(sorting_list)):
        for j in range(i, 0, -1):
            if sorting_list[j] < sorting_list[j-1]:
                sorting_list[j], sorting_list[j-1] = sorting_list[j-1], sorting_list[j]
            else:
                break
##################시간 복잡도 O(n2)
##################공간복잡도 O(N)

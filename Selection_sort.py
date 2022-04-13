def selection_sort(sorting_list):
    for i in range(len(sorting_list)):
        min_index = i  
        for j in range(i+1,len(sorting_list)):
            if sorting_list[j] < sorting_list[i]:
                min_index = j
        sorting_list[i], sorting_list[min_index] = sorting_list[min_index], sorting_list[i]
 #선택정렬 가장 작은 index를 탐색후 정렬
        
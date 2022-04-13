def quick_sort(sorting_list, start,end):
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left<=right):
        while(left<=end and sorting_list[pivot]>=sorting_list[left]):
            left+=1
        while(right>=start and sorting_list[pivot]<= sorting_list[right]):
            right-=1
        if(left>right):
            sorting_list[right], sorting_list[pivot] = sorting_list[pivot], sorting_list[right]
        else:
            sorting_list[right], sorting_list[left] = sorting_list[left], sorting_list[right]
        
    quick_sort(sorting_list, start, right-1)
    quick_sort(sorting_list, right, end)

sorted_list = [1,2,3,4,5,6]
quick_sort(sorted_list, 0, len(sorted_list)-1)
#공간복잡도 O(N)
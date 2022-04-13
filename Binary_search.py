
#################################################################반복문 구현
def binary_search(sorting_list, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    while(start<=end):
        if sorting_list[mid] == mid:
            return mid
        elif sorting_list[mid]>mid:
            end = mid-1
        else:
            start =mid+1
    return None
   
####################################################################재귀적구현    
def binary_search(sorting_list, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    
    if sorting_list[mid] == mid:
        return mid
    elif sorting_list[mid]>mid:
        binary_search(sorting_list, target, start, mid-1)
    else:
        binary_search(sorting_list, target, mid+1, end)

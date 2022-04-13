def counting_sort(sorting_list):
    count = [0] * (max(sorting_list)+1)
    for i in range(len(sorting_list)):
        count[sorting_list[i]]+=1
    for i in range(len(count)):
        for _ in range(count[i]):
            print(i, end=' ')

######################################################
#시간복잡도 O(N+K) 데이터의 크기가 한정되어 있을때 
#공간복잡도 O(N+K)
######################################################

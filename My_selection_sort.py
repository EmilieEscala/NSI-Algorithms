def my_selection_sort(t):
    res=[0]*len(t)
    j=index_of_the_smallest(t)
    for i in range(len(t)):
        res[i]=t[j]
        remove(t,j)
    return res
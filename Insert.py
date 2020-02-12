def insert(t,i):
    for index in range(i,0,-1):
        if t[index]<t[index-1]:
            swap(t, index-1, index)
        else:
            break

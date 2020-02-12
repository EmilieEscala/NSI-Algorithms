def element_of_the_smallest(list,start,stop):
    if start >= stop:
        fin=start
        debut=stop
    else:
        fin=stop
        debut=start
    for element in list:

        if element >= debut and element <= fin:
            print (element)
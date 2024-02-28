# selection sort

array = [3, 2, 1, 3, 0, 6, -5645, -2, 343242, 767886675, 3, 4, 3, 4, 5]

def selection_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)): 
            if lst[j] < lst[i]:
                (lst[i], lst[j]) = (lst[j], lst[i]) #neat way of swapping values
    return lst

print(selection_sort(array))


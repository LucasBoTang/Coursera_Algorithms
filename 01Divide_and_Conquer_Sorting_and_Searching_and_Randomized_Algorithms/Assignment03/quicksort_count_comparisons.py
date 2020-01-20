from statistics import median

def quick_sort(ints, l, r, pivot_method):
    """
    quick sort with different pivot method
    compute the number of comparisons
    """
    # base case
    if l >= r:
        return ints, 0
    # get pivot
    p_ind = pivot_method(ints, l, r)
    p = ints[p_ind]
    ints[l], ints[p_ind] = ints[p_ind], ints[l]
    # partition around pivot
    i = l + 1
    for j in range(i, r+1):
        if ints[j] < p:
            ints[i], ints[j] = ints[j], ints[i]
            i += 1
    ints[l], ints[i-1] = ints[i-1], ints[l]
    p_ind = i - 1
    # sort recursively
    _, com_l = quick_sort(ints, l, p_ind-1, pivot_method)
    _, com_r = quick_sort(ints, p_ind+1, r, pivot_method)
    return ints, r - l + com_l + com_r

# load txt as int list
ints = []
with open('./QuickSort.txt', 'r') as f:
    for line in f:
        ints.append(int(line.rstrip()))
n = len(ints) -  1

# use the first element of the array as the pivot element
_, nums = quick_sort(ints.copy(), 0, n, lambda ints, l, r: l)
print('Number of comparisons for first element pivot:', nums)

# use the last element of the array as the pivot element
_, nums = quick_sort(ints.copy(), 0, n, lambda ints, l, r: r)
print('Number of comparisons for last element pivot:', nums)

# use the median-of-three pivot rule
def median_of_three(ints, l, r):
    """
    get the middle of the first, middle, and final elements of the given array
    """
    three = [ints[l], ints[(l+r)//2], ints[r]]
    three_ind = three.index(median(three))
    return [l, (l+r)//2, r][three_ind]
_, nums = quick_sort(ints.copy(), 0, n, median_of_three)
print('Number of comparisons for median_of_three pivot:', nums)

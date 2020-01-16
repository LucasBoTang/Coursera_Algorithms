def count_inversions(ints):
    """
    count inversions with mergesort
    """
    # base case
    n = len(ints)
    if n == 1:
        return 0, ints
    # count left and right half recursively
    nums_l, sort_l = count_inversions(ints[:n//2])
    nums_r, sort_r = count_inversions(ints[n//2:])
    # mersort and count split inversions
    nums_s = 0
    sort = []
    while sort_l and sort_r:
        if sort_l[0] > sort_r[0]:
            nums_s += len(sort_l)
            sort += sort_r[:1]
            sort_r = sort_r[1:]
        else:
            sort += sort_l[:1]
            sort_l = sort_l[1:]
    sort += sort_l + sort_r
    return nums_l + nums_r + nums_s, sort

# load txt as int list
ints = []
with open('./IntegerArray.txt', 'r') as f:
    for line in f:
        ints.append(int(line.rstrip()))
nums, _ = count_inversions(ints)

print("Number of the inversions:", nums)

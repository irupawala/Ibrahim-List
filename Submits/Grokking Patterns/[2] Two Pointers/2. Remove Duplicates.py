# Grokking - Problem 2 in Two Pointers
# Question is a Google Interview Question. Note that array is not sorted and it is done in-place

def remove_duplicates(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1
    
    i = 0
    while(i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()

'''
Time Complexity - O(N)
Space Complexity - O(1)
'''

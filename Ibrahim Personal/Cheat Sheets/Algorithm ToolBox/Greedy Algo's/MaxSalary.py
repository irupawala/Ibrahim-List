# python3

def IsGreaterOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def largestnumber(lst):
    answer = []
    
    while lst!=[]:
        max_digit = 0
        for digit in lst:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)

    return answer


if __name__ == "__main__":
    n = int(input())
    lst = [int(i) for i in input().split()]
    print(''.join([str(i) for i in largestnumber(lst)]))
    

"""

Time Complexity - O(n*n)

"""        
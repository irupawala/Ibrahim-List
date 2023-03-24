def find_unique(lst):
    result = []
    for i in lst:
        if 2*i in lst and lst.count(2*i) == 1:
            result.append(i)
    result.sort()        
    print(*(result))
    
if __name__ == "__main__":
    find_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 8])
    find_unique([7, 17, 11, 1, 23])
    find_unique([1, 1, 2])
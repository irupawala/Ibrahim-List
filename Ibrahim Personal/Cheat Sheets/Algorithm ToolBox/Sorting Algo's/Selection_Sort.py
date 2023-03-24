if __name__ == "__main__":
    
    input_array = list(map(int, input().split()))
    distinct_integers = int(input())
    sorted_array = []
    
    count = [0] * distinct_integers
    
    for i in input_array:
        count[i-1] += 1
        
    for index, number in enumerate(count):
        for x in range(number):
            sorted_array.append(index+1)
            
            
    print(sorted_array)
        
'''

Time Complexity - O(n^2)
    
'''
import random

def scoring(number):
    str_number = str(number)
    list_number = [int(x) for x in str_number]
    total_points = 0
    
    # points for 9
    nine_points = list_number.count(9)
    total_points += (nine_points*4)
    
    # points for 7 multiple
    if number % 7 == 0:
        total_points += 1
        
    # points for even number
    for no in list_number:
        if no % 2 == 0:
            total_points += 2
              
    # points for consecutive numbers
    j = 0
    while j < len(list_number):
        sequence_length = 0
        while j < len(list_number)-1 and list_number[j+1] == list_number[j]+1:
            sequence_length += 1
            j += 1

        total_points += (sequence_length+1)**2
        
        j += 1            

    # points for consecutive ones
    i = 0
    while i < len(list_number):
        one_counts = 0
        while i < len(list_number)-1 and list_number[i] == 1 and list_number[i+1] == 1:
            one_counts += 1
            i += 1 
        if one_counts > 0:
            total_points += ((one_counts)*5) # for pairs
            if one_counts+1 > 2:
                total_points += ((one_counts+1-2)*5)
        
        i += 1

    return total_points



def NumberScores(num):
    # TODO: Write your code here
    num_int = num
    score = 0
    num = str(num)
    num = list(num)
    num = [int(n) for n in num]
    #print(num)
    
    #Multiple of 7
    if num_int%7 == 0: score += 1
    
    for no in num:
        # points for 9
        if no == 9:
            score += 4
        # Even no
        elif no%2 == 0:
            score += 2
            
    # points for consecutive ones
    i = 0
    while i < len(num):
        one_counts = 0
        while i < len(num)-1 and num[i] == 1 and num[i+1] == 1:
            one_counts += 1
            i += 1 
        if one_counts > 0:
            score += ((one_counts)*5) # for pairs
            if one_counts+1 > 2:
                score += ((one_counts+1-2)*5)
        
        i += 1
    
    # points for consecutive numbers
    j = 0
    while j < len(num):
        sequence_length = 0
        while j < len(num)-1 and num[j+1] == num[j]+1:
            sequence_length += 1
            j += 1

        score += (sequence_length+1)**2
        
        j += 1  
        
    
    return score



while True:
    n = random.randint(0, 10000000000)
    res1 = scoring(n)
    res2 = NumberScores(n)
    
    if res1 != res2:
        print(f"Wrong Answer for n = {n}")
        print (f"res1 = {res1}, res2 = {res2}")
        break
    else:
        print (f"Results Matched for n = {n}")
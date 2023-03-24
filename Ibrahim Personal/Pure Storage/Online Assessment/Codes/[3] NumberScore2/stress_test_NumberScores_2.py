import random

def scoring(number):
    str_number = str(number)
    list_number = [int(x) for x in str_number]
    total_points = 0
    
    # points for 7
    seven_points = list_number.count(7)
    total_points += seven_points
    
    # points for 3 multiple
    if number % 3 == 0:
        total_points += 2
        
    # points for even number
    for no in list_number:
        if no % 2 == 0:
            total_points += 4
              
    # points for consecutive numbers
    j = 0
    while j < len(list_number):
        sequence_length = 0
        while j < len(list_number)-1 and list_number[j+1] == list_number[j]-1:
            sequence_length += 1
            j += 1

        total_points += (sequence_length+1)**2
        
        j += 1            

    # points for consecutive fives
    i = 0
    while i < len(list_number):
        five_counts = 0
        while i < len(list_number)-1 and list_number[i] == 5 and list_number[i+1] == 5:
            five_counts += 1
            i += 1 
        if five_counts > 0:
            total_points += ((five_counts)*3) # for pairs
            if five_counts+1 > 2:
                total_points += ((five_counts+1-2)*3)
        
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
    
    #Multiple of 3
    if num_int%3 == 0: score += 2
    
    for no in num:
        # points for 9
        if no == 7:
            score += 1
        # Even no
        elif no%2 == 0:
            score += 4
            
    i = 0
    fives_len = 0
    # search for consequitive 5's
    while i < len(num):
        fives_len = 1
        if num[i] == 5:
            while i < len(num)-1 and num[i+1] == 5:
                fives_len += 1
                i += 1
        if fives_len > 1:
            score += 3*(fives_len-1)
            score += 3*(fives_len-2)
            
        i += 1
    
    j = 0
    consecutive_len = 1
    while j < len(num):
        consecutive_len = 1
        
        while j < len(num)-1 and num[j]-num[j+1] == 1:
            consecutive_len += 1
            j += 1
            
        if consecutive_len > 1:
            score += (consecutive_len**2)
        else:
            score += 1

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
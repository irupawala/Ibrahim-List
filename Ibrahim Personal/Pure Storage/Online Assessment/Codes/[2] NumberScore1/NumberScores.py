
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

def main():
  print(NumberScores(11129))
main()


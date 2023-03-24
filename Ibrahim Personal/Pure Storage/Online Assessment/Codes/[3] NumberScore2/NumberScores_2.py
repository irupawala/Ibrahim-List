
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

def main():
  print(NumberScores(8555356638))
main()


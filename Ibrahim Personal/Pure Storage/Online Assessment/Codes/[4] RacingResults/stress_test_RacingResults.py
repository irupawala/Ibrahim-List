import random

def racing_results(lst):
    winner = [0, 0] # racer_name, total_points
    
    points_table = {1:10, 2:6, 3:4, 4:3, 5:2, 6:1}
    racer_points = {} # racer_name : total_points
    zero_points_racer = []
    
    for i in lst:
        race, racer_name, position = i[0], i[1], i[2]
        racer_points[racer_name] = racer_points.get(racer_name, 0) + points_table.get(position, 0)
        
        current_racer_total = racer_points[racer_name]
        winner_racer_name = winner[0]
        winner_racer_total = winner[1]
        
        if current_racer_total > winner_racer_total:
            winner = [racer_name, current_racer_total]
        elif current_racer_total == winner_racer_total:
            if racer_name < winner_racer_name:
                winner = [racer_name, current_racer_total]
                
        if racer_name in zero_points_racer and current_racer_total != 0:
            zero_points_racer.remove(racer_name)
            
        if current_racer_total == 0 and racer_name not in zero_points_racer:
            zero_points_racer.append(racer_name)
    '''            
    for key, value in racer_points.items():
        if value == 0: # racer with 0 points
            zero_points_racer.append(key)
    '''
    zero_points_racer.sort()            
    return (winner, zero_points_racer)


def generate_generalized_abbreviation(nums):
    # TODO: Write your code here
    racer_zero_point = set()
    racer_points = {}
    
    points_dict = {1:10, 2:6, 3:4, 4:3, 5:2, 6:1} #position, points
    max_racer, max_points = 0, 0
    
    for i in range(len(nums)):
        racer = nums[i][1]
        position = nums[i][2]
        total_points = racer_points.get(racer, 0) + points_dict.get(position, 0)
        racer_points[racer] = total_points
        
        if total_points > max_points:
            max_points = total_points
            max_racer = racer
        elif total_points == max_points:
            if racer < max_racer:
                max_racer = racer
                
            
    for i in racer_points:
        if racer_points[i] == 0:
            racer_zero_point.add(i)
    
    racer_zero_point = list(racer_zero_point)        
    racer_zero_point.sort()
    return ([max_racer, max_points], racer_zero_point)



while True:
    n = random.randint(3, 100)
    lst = []
    
    for i in range(n):
        lst.append([random.randint(2001, 2101), random.randint(1001, 1101), random.randint(1, 15)])
    
    
    res1 = racing_results(lst)
    res2 = generate_generalized_abbreviation(lst)
    
    if res1 != res2:
        print(f"Wrong Answer for lst = {lst}")
        print (f"res1 = {res1}, res2 = {res2}")
        break
    else:
        print (f"Results Matched for lst = {lst}")
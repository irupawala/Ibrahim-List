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

def main():
  #print(generate_generalized_abbreviation([[2001, 1001, 3], [2001, 1002, 2], [2002, 1003, 1], [2002, 1001, 2], [2002, 1002, 3], [2001, 1003, 1]]))
  print(generate_generalized_abbreviation([[2001, 1001, 7], [2001, 1002, 7], [2002, 1003, 8], [2002, 1001, 8], [2002, 1002, 3], [2001, 1003, 6]]))
main()

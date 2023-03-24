

def generate_generalized_abbreviation(nums):
    result = []
    # TODO: Write your code here
    for i in range(len(nums)):
        double = nums[i]*2 
        if double in nums and nums.count(double) == 1:
            result.append(nums[i])
    
    result.sort()
    return result


def main():
  #print(generate_generalized_abbreviation([1,2,3,4,5,6,7,8,9,0,8]))
  
  #print(generate_generalized_abbreviation([7,17,11,1,23]))
  
  #print(generate_generalized_abbreviation([1,1,2]))
  
  print(generate_generalized_abbreviation([1,1,1, 2, 2, 4,8,0]))

main()

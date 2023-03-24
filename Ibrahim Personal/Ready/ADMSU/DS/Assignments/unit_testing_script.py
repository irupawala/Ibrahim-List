############################################# Unit Testing ###############################################
    
import os     
def test():
    

    filename_list = []
    for root, dirs, files in os.walk("./tests"):
        for filename in files:
#            if '.a' not in filename:
            if not filename.endswith('.a'): 
                filename_list.append(filename)
                filename_list.sort()
                
    for filename in filename_list:
        
        print('........................')
        print('Running Test: ' + filename)
            
        f=open("./tests/" + filename, "r")
        if f.mode == 'r':
            test_input = f.read().rstrip('\n')
            f.close()
        f=open("./tests/" + filename + '.a', "r")
        if f.mode == 'r':
            expected_output =f.read().rstrip('\n')
            f.close()
            
        output = find_mismatch(test_input) # Change the code here
        
 
        print('Input: ' + str(test_input))
        print('Expected Output: ' + str(expected_output))
        print('Ouput: ' + str(output))



        if str(expected_output)==str(output):
            print('Test Passed')
        else:
            print('Test Failed')
            break    

    print("Passed all tests !!")
       

#############################################################################################################
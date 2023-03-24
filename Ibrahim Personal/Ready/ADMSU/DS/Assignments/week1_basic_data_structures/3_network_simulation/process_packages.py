# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


'''
Running time - O(n_requests)
'''

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here        
        if len(self.finish_time) != 0 and self.finish_time[0] <= request.arrived_at: # If the first item could be removed, remove it first
            self.finish_time.pop(0)           
                     
        if len(self.finish_time) < self.size: 
            if len(self.finish_time) == 0: started_at = request.arrived_at  # If buffer is empty start immediately            
            else: started_at = self.finish_time[-1] # else start time is the finish of the last process
            was_dropped = False
            self.finish_time.append(started_at + request.time_to_process)
        else:
            was_dropped = True
            started_at = -1        
            
        return Response(was_dropped, started_at)  


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


############################################# Unit Testing ###############################################
    
import os     
def test():
    

    filename_list = []
    for root, dirs, files in os.walk("./tests"):
#    for root, dirs, files in os.walk("./test_case"):
        for filename in files:
#            if '.a' not in filename:
            if not filename.endswith('.a'): 
                filename_list.append(filename)
                filename_list.sort()
                
    for filename in filename_list:
        
        print('........................')
        print('Running Test: ' + filename)
            
        f=open("./tests/" + filename, "r")
#        f=open("./test_case/" + filename, "r")        
        if f.mode == 'r':
            
            
            ###############################################################
            test_input = f.read().rstrip('\n')
            f.close()
            lines =  test_input.splitlines()
            n = lines[0]
            requests = []
            output_list = []
            buffer_size, n_requests = map(int, n.split())
            for i in range(1, n_requests+1):
                arrived_at, time_to_process = map(int, lines[i].split())
                requests.append(Request(arrived_at, time_to_process))   
            
            buffer = Buffer(buffer_size)
            responses = process_requests(requests, buffer)
            
            for response in responses:
                if not response.was_dropped:                 
                    output_list.append(response.started_at)
                else:
                    output_list.append(-1)
                    

#            output = " ".join(map(str,output_list))       
#            print(f"output = {output}")  

            ###############################################################


        f=open("./tests/" + filename + '.a', "r")
#        f=open("./test_case/" + filename + '.a', "r")        
        if f.mode == 'r':
            expected_output = f.read().split('\n')
            expected_output = list(map(int, expected_output[:-1]))
            f.close()
            
        print('Expected Output: ' + str(expected_output))
        print('Ouput: ' + str(output_list))

        
        if str(expected_output) == str(output_list):
            print(f'Test {filename} Passed')
        else:
            print(f'Test {filename} Failed')
            break   
        
        
if __name__ == "__main__":
     main()
#    test()
        
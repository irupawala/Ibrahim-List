# python3
#import sys

'''
Running Time - O(|Text| + |Text|)
Space  - O(2|Text|)
'''


def BWT(text):
     
    patterns_list = []
    bwt_text = ""
    
    for x in range(len(text)):
       text = text[-1] + text[:len(text)-1]
       patterns_list.append(text)        
    
    sorted_string = sorted(patterns_list)

    for x in sorted_string:
        bwt_text = bwt_text + x[-1]
    
    return bwt_text

if __name__ == '__main__':
#    text = sys.stdin.readline().strip()
    
    text = input()
    print(BWT(text))
# python3
#import sys

def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp

def rightrotate(s, d):
   
   return leftrotate(s, len(s) - d)

def BWT(text):
     
    patterns_list = []
    bwt_text = ""
    
    for x in range(len(text)):
       text = rightrotate(text, 1) 
       patterns_list.append(text)        
    
    sorted_string = sorted(patterns_list)

    for x in sorted_string:
        bwt_text = bwt_text + x[-1]
    
    return bwt_text

if __name__ == '__main__':
#    text = sys.stdin.readline().strip()
    
    text = input()
    print(BWT(text))
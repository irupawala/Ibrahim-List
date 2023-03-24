import random

def itemMismatch(lst):
    count = 0
    
    for l in lst:
        word1, word2 = l
        word1_set, word2_set = list(set(word1)), list(set(word2))

        if len(word1_set) != len(word2_set):
            count += 1
            
        else:
            
            for i in range(len(word1_set)):
                letter = word1_set[i]
                if word1.count(letter) != word2.count(letter):
                    count += 1
                    break
                
    return count 

def stress_test():
    acceptable_letters = ["c", "m"]
    for i in range(10):
        word_len = random.randrange(1, 5)
        list_len = random.randrange(1, 5)
        input_list = []
        word1 = "".join(map(str, [random.choice(acceptable_letters) for i in range(word_len)]))
        word2 = "".join(map(str, [random.choice(acceptable_letters) for i in range(word_len)]))
        for i in range(list_len):
            input_list.append([word1, word2])
            print(input_list)
            print(itemMismatch(input_list))
            
if __name__ == "__main__":
    #print(itemMismatch([["cm", "mc"], ["ccm", "mc"], ["pm", "mc"], ["c", "mc"]]))
    #print(itemMismatch([["cccmm", "mmccc"], ["ccm", "mcc"], ["pppm", "mc"], ["ccmcc", "mcccc"]]))
    stress_test()

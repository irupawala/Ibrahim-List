def isSatisfiable(n, clauses):
# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.      +
    result_list = []
    for mask in range(1<<n):

        result = [ (mask >> i) & 1 for i in range(n) ]
        formulaIsSatisfied = True
        result_bool = ("".join(map(str,result)))
        print(result_bool)
        for clause in clauses:
            clauseIsSatisfied = False
            
            print("".join(map(str,clause)))
            
            if (clause[0] < 0) :
                 if (result[abs(clause[0]) - 1] == 0): 
                    clauseIsSatisfied = True  
            else:
                if (result[abs(clause[0]) - 1] == 1): 
                    clauseIsSatisfied = True  

            if (clause[1] < 0) :
                 if (result[abs(clause[1]) - 1] == 0): 
                    clauseIsSatisfied = True  
            else:
                if (result[abs(clause[1]) - 1] == 1): 
                    clauseIsSatisfied = True  
                    
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
#                print("------------------------------------------------------------------------------")
#                break
        if formulaIsSatisfied:
            result_list.append(result_bool)
    print(result_list)
#            return result
    return None


if __name__ == "__main__":

    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]
    
    result = isSatisfiable(n, clauses)
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        result_list = [-i-1 if result[i] else i+1 for i in range(n)]
        print(" ".join(map(str, result_list)))

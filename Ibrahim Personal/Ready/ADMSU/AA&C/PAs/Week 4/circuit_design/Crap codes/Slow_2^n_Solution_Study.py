def isSatisfiable(n, clauses):

    for mask in range(1<<n):
        result = [ (mask >> i) & 1 for i in range(n) ]
        formulaIsSatisfied = True
        print("".join(map(str,result))[::-1])
        for clause in clauses:
            clauseIsSatisfied = False
            
            print("".join(map(str,clause)))
#            print("------------------------------------------------------------------------------")
            print(f"clause_0={clause[0]}  abs_clause_0={abs(clause[0])}  abs_clause_0_min1={abs(clause[0]) - 1} result_abs_clause_0_min1={bool(result[abs(clause[0]) - 1])} clause[0]<0={(clause[0] < 0)}")
#            print(f"result_0 = {result[abs(clause[0]) - 1] == (clause[0] < 0)}")
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clauseIsSatisfied = True  
#            print(f"CS_0 = {clauseIsSatisfied}")    
#            print(f"result_1 = {result[abs(clause[1]) - 1] == (clause[1] < 0)}")
            print(f"clause_1={clause[1]}  abs_clause_1={abs(clause[1])}  abs_clause_1_min1={abs(clause[1]) - 1} result_abs_clause_1_min1={bool(result[abs(clause[1]) - 1])} clause[1]<0={(clause[1] < 0)}")
            if result[abs(clause[1]) - 1] == (clause[1] < 0):    
                clauseIsSatisfied = True
#            print(f"CS_1 = {clauseIsSatisfied}")                 
            print(f"clauseIsSatisfied_Final = {clauseIsSatisfied}")       
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
                print("------------------------------------------------------------------------------")
                break
        if formulaIsSatisfied:
            return result
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

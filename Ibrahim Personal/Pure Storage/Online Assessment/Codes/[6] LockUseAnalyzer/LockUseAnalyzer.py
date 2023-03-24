from collections import deque

def lock_analyzer(lst):
    # TODO: Write your code here
    q = deque()
    N = 0
    
    for _in in lst:
        command = _in[0]
        lock = _in[1]
        
        if command == "ACQUIRE":
            if lock in q:
                return N+1
            else:
                N += 1
                q.append(lock)
        elif command == "RELEASE":
            if lock not in q:
                return N+1
            else:
                popped_lock = q.pop()
                if popped_lock != lock: return N+1
                else:
                    N += 1
                
                
    return len(q)+1 if len(q) != 0 else 0

def main():
  print(lock_analyzer([["ACQUIRE", 123], ["ACQUIRE", 364], ["ACQUIRE", 84], ["RELEASE", 84], ["RELEASE", 364], ["ACQUIRE", 789], ["RELEASE", 456], ["RELEASE", 123]]))
  print(lock_analyzer([["ACQUIRE", 364], ["ACQUIRE", 84], ["ACQUIRE", 364],["RELEASE", 364]]))
  print(lock_analyzer([["ACQUIRE", 364], ["ACQUIRE", 84], ["RELEASE", 84],["RELEASE", 364]]))
  print(lock_analyzer([["ACQUIRE", 364], ["ACQUIRE", 84], ["RELEASE", 84],["RELEASE", 364],["ACQUIRE", 364], ["ACQUIRE", 84]]))
  print(lock_analyzer([["RELEASE", 84],["RELEASE", 364]]))
  print(lock_analyzer([["ACQUIRE", 364], ["ACQUIRE", 84], ["RELEASE", 364],["RELEASE", 84]]))
main()


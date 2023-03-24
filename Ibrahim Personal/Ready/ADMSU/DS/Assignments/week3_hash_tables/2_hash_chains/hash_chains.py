# python3



'''
Amortized Running time is O(1 + α). However worst-case time complexity can be O(n)
'''


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count): # here bucket_count is the cardinality factor
        self.bucket_count = bucket_count
        # store all strings in one list
        # self.elems = []
        self.key = 0
        self.hashTable = [[] for _ in range(bucket_count)]
        

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            print(ord(c))
            print(ans * self._multiplier)
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            # self.write_chain(cur for cur in reversed(self.elems) if self._hash_func(cur) == query.ind)
            self.write_chain(cur for cur in reversed(self.hashTable[query.ind]))
        else:
            self.key = self._hash_func(query.s)
            try:
                #ind = self.elems.index(query.s)
                ind = self.hashTable[self.key].index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                   #self.elems.append(query.s)
                   self.hashTable[self.key].append(query.s)
            else:
                if ind != -1:
                    #self.elems.pop(ind)
                    self.hashTable[self.key].pop(ind)
        
        #print(self.hashTable)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)  # here bucket_count is the cardinality factor
    proc.process_queries()

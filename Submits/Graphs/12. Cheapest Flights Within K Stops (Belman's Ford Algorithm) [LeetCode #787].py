LeetCode Link - https://leetcode.com/problems/cheapest-flights-within-k-stops/

# Belman's Ford Algorithm for finding shortest path with negative edges

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k) :
        adj_list = {i: [] for i in range(n)}
        dist_dict = {i:float("inf") for i in range(n)}
        dist_dict[src] = 0
        
        for u, v, dist in flights:
            adj_list[u].append((v, dist)) # node, dist

        for no_of_iterations in range(k+1):
            temp_dict = dist_dict.copy()
            for node in adj_list.keys():
                for nei, cost in adj_list[node]:
                    if temp_dict[nei] > dist_dict[node] + cost:
                        temp_dict[nei] = dist_dict[node] + cost
            dist_dict = temp_dict

        return dist_dict[dst] if dist_dict[dst] != float("inf") else -1

'''
Time Complextiy - O(E.k)
Space Complexity - O(n) for storing dist_dict
'''

# NeetCode Solution 
'''
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k) :
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]
'''

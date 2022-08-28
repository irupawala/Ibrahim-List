class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        # base case: if the expression string is a number, parse and add it to output.
        if '+' not in expression and '-' not in expression and '*' not in expression:
            result.append(int(expression))
        else:
            for i in range(0, len(expression)):
                char = expression[i]
                if not char.isdigit():
                    # break the equation here into two parts and make recursively calls
                    leftParts = self.diffWaysToCompute(expression[0:i])
                    rightParts = self.diffWaysToCompute(expression[i+1:])
                    for part1 in leftParts:
                        for part2 in rightParts:
                            if char == '+':
                                result.append(part1 + part2)
                            elif char == '-':
                                result.append(part1 - part2)
                            elif char == '*':
                                result.append(part1 * part2)
        return result        

'''
Time Complexity - O(N.2^N)
Space Complexity - O(N.2^N)
'''

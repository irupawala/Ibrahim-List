# python3


def maxPrizes(n):
    prizeList = []
    prize = 1
    while n > 0:
        n -= prize
        if prize < n:
            prizeList.append(prize)
        else:
            prizeList.append(n+prize)
            n = 0
        prize += 1
        
    return prizeList


if __name__ == "__main__":
    n = int(input())
    maxPrizeList = maxPrizes(n)
    print(len(maxPrizeList))
    print(*maxPrizeList)
def recMC(coinValueList,change):
    minCoins=change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC(coinValueList,change-i)
            if numCoins<minCoins:
                minCoins=numCoins
    return minCoins

print(recMC([1,5,10,21,25],63))


def recMC(coinValueList,change,knownResults):
    minCoins=change
    if change in coinValueList:
        return 1
    elif knownResults[change]>0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC(coinValueList,change-i,knownResults)
            if numCoins<minCoins:
                minCoins=numCoins
                knownResults[change]=minCoins
    return minCoins

print(recMC([1,5,10,21,25],63,[0]*64))
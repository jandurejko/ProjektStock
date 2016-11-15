
def infoSaamineCSVFailist(stockName, mituVäljundit):
    fail = stockName + ".csv"
    f = open(fail)
    mituPäevaKorraga = mituVäljundit
    pealkirjad = f.readline().strip().split(',')
    dateTitle = pealkirjad[0]
    openTitle = pealkirjad[1]
    #highTitle = pealkirjad[2]
    #lowTitle = pealkirjad[3]
    #closeTitle = pealkirjad[4]
    #volumeTitle = pealkirjad[5]
    #adjCloseTitle = pealkirjad[6]

    for i in range(mituPäevaKorraga):
        andmed = f.readline().strip().split(',')
        kuupäev = andmed[0]
        avatud = andmed[1]
        print(dateTitle + ': ' + kuupäev + ' ' + openTitle + ': ' + avatud)
    f.close()



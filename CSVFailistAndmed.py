def reverseCSV(stockName):
    fail = stockName + ".csv"
    tekst = ""
    f = open(fail)
    tekst += f.readline()
    f.close()
    for line in reversed(list(open(fail))):
        tekst += line
    f = open(fail, 'w')
    f.write(tekst)
    f.close()

def infoSaamineCSVFailist(stockName, mituVäljundit):
    reverseCSV(stockName)
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
    arvudInimesele = {}
    arvudKeskmiseJaoks = {}


    for i in range(mituPäevaKorraga):
        andmed = f.readline().strip().split(',')
        kuupäev = andmed[0]
        avatud = andmed[1]
        arvudInimesele[kuupäev] = avatud
        #print(dateTitle + ': ' + kuupäev + ' ' + openTitle + ': ' + avatud)
    for i in range(200):
        andmed = f.readline().strip().split(',')
        kuupäev = andmed[0]
        avatud = andmed[1]
        arvudKeskmiseJaoks[kuupäev] = avatud

    f.close()
    return arvudInimesele, arvudKeskmiseJaoks





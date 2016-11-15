from pandas_datareader import data
import time
import os
def stockToCSV(stockname):
    stockName = stockname
    dirpath = os.path.dirname(__file__)
    aasta = int(time.strftime("%Y")) - 1
    kuu = time.strftime("%m")
    päev = time.strftime("%d")
    kuupäev = str(aasta) + "-" + str(kuu) + "-" + str(päev)


    stockInfo = data.DataReader(stockName, 'yahoo', kuupäev)
    stockInfo.to_csv(dirpath + "/" + stockName + ".csv")

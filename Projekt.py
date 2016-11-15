from CSVFailistAndmed import infoSaamineCSVFailist
from InfoSaamineNetist import stockToCSV


stockname = "AMD"#Selle lahti peaks saama kasutaja valida tinkeris(mingi 3-4 valikut)
mitupäeva = 10 #mitut päeva soovib kasutaja näha, siin ka valik mis tuleb tinkerist
stockToCSV(stockname)#loob sinna kausta, kus asub praegune .py file stockname nime järgi csv faili kus on andmed sees
                     #1 aasta jagu, seda saab muuta InfoSaamineNetist failis
infoSaamineCSVFailist(stockname, mitupäeva)#hetkel csv fail on valepidi, ehk vanemast -> uuemani, katsun fix leida

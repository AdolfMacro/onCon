from requests import get
from os import system
from platform import system as osType
from colorama import Fore

def getPrice(base):
    def regPrice(url):
        response = get(url)
        data = response.json()
        return data
                
        

    return {
        "BTC": regPrice(f"https://api.binance.com/api/v3/ticker/price?symbol=BTC{base}" ) ,
        "BNB": regPrice(f"https://api.binance.com/api/v3/ticker/price?symbol=BNB{base}") ,
        "ETH": regPrice(f"https://api.binance.com/api/v3/ticker/price?symbol=ETH{base}") ,
        "XRP": regPrice(f"https://api.binance.com/api/v3/ticker/price?symbol=XRP{base}") ,
        "ADA": regPrice(f"https://api.binance.com/api/v3/ticker/price?symbol=ADA{base}") ,
        "SOL": regPrice(f"https://api.binance.com/api/v3/ticker/price?symbol=SOL{base}") ,
        "DOGE": regPrice(f"https://api.binance.com/api/v3/ticker/price?symbol=DOGE{base}") ,
        "DOT": regPrice(f"https://api.binance.com/api/v3/ticker/price?symbol=DOT{base}") ,
        "MATIC": regPrice(f"https://api.binance.com/api/v3/ticker/price?symbol=MATIC{base}") ,
    }
    


def putIn(mainStr):
    ceiling=(f"{Fore.LIGHTRED_EX}╔══╗" , f"{Fore.LIGHTRED_EX}╗")
    main=f"{Fore.LIGHTBLUE_EX}║  "
    floor=(f"{Fore.LIGHTRED_EX}╚══╝" , f"{Fore.LIGHTRED_EX}╝")
    charMain=f"{Fore.LIGHTBLUE_EX}═"
    count=len(mainStr)+2
    return f"{ceiling[0][0:-1]+charMain*count+ceiling[1]}\n{main+mainStr+'  ║'}\n{floor[0][0:-1]+charMain*count+floor[1]}"
def mainPic(tables):
    res=""
    for i in tables.split("\n"):    
        res+=(" "*5)+i+'\n'
    return res

def merge(items):
    res={
        1:"",
        2:"",
        3:""
    }

    for i in range(3):
        for j in range(0 , len(items) , 3):
            for y in range(j-3 , j):
                res[i+1]+=items[y].split("\n")[i]
    fres=""
    for i in res.keys():
        fres+=res[i]+"\n"
    return fres
def clear():
    if "windows" in osType():
        system("cls")
    else :
        system("clear")
def launcher(base , sg):
    banner=f"""
    {Fore.LIGHTRED_EX}╔═══════════════════════════════════════════════════════╗
    {Fore.LIGHTRED_EX}║{Fore.LIGHTGREEN_EX} Welcome, developed by {Fore.LIGHTRED_EX}AdolfMacro{Fore.LIGHTRED_EX}                      ║
    ║                                    {Fore.LIGHTGREEN_EX}Ctrl+C : Main menu {Fore.LIGHTRED_EX}║
    {Fore.LIGHTRED_EX}╚═══════════════════════════════════════════════════════╝{Fore.RESET}

"""
    data=getPrice(base)
    tables=[]
    
    for i in data.keys():
        tables.append(putIn(i+" : "+("%.2f" %float(data[i]["price"])+sg)))
    resTable=""
    for i in range(3 , len(tables)+3 , 3):
        resTable+=merge([tables[i-1] , tables[i-2] , tables[i-3]])
    clear()
    print(banner+mainPic(resTable))

def main():
    base="USDT"
    sg="$"
    while 1:
        try:
            launcher(base  , sg)
        except KeyboardInterrupt:
            while 1:
                clear()
                selection=input("""
1. USD      2. EUR
3. Back     4. Exit


Enter you'r selection : """)
                try :
                    int(selection)
                    if selection=="1":
                        base="USDT"
                        sg="$"
                        break
                    elif selection=='2':
                        base="EUR"
                        sg="€"
                        break
                    elif selection=='4':
                        return 1
                    else:
                        break

                except :
                    pass
        
if __name__=="__main__":
    main()
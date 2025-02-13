import requests
from bs4 import BeautifulSoup
import time


    
    
    
def gethtml(url, name):
    headers = {
        'user-agent' : 'Mozilla/5.0'
    }
    a = name
    r = requests.get(url + "stkNo=%s"%a, headers = headers, timeout = 30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

      
def writedown(html, file, ulist):

    try:
        
        soap = BeautifulSoup(html, "html.parser")
        content = soap.tbody.tr('td')
        title = ["本日漲停:", "開盤競價基準:", "本日跌停:"]
        company = str(soap.find(id = "csvTitle2")).strip('<a id="csvTitle2"><h2>').strip('</h2>')
        for num in content:       
            ulist.append(str(num).strip('<td>').strip('</td>'))      

        file.write(company + title[0]  + ulist[0] + title[1] + ulist[1] + title[2] + ulist[2] + '\n')
    except:
        print("出現未知錯誤")

def main():
    i = 0
    name = []

    while (True): 
        name.append(input("請輸入代號，按0結束:"))
        i = i+1 
        print(name[i-1])
        if (name[i-1] == '0'):
            name.pop()
            i = i-1
            break

  
    f = open("stock.txt", "w", encoding = "utf-8")
 
    ulist = []
    for count in range(i):
        url = "https://www.twse.com.tw/zh/stockSearch/showStock?"
        gethtml(url, name[count])
        writedown(gethtml(url, name[count]), f, ulist)
        

    f.close()
    print("下載成功")
    time.sleep(2)
main()    


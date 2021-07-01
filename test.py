import requests
from bs4 import BeautifulSoup


def search(keyword):
    url = 'https://www.momomall.com.tw/mmlsearch/%s.html'
    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    r = requests.post(url % keyword, headers=headers, timeout=10)
    r.raise_for_status()
    r.encoding = 'UTF-8'
    return r.text


def gethtml(html, list, list2):
    soap = BeautifulSoup(html, 'html.parser')
    price = soap.find_all('p', class_='prdPrice')
    name = soap.find_all(class_='prdName')
    for x in name:
        list.append(str(x))
    for i in price:
        list2.append(str(i))


def writeinfo(list, list2, f):
    priz = []
    print(list2[5])
    for num in range(len(list)):
        f.write('商品名稱:')
        f.write(str(list[num]))
        f.write('\n')
        f.write('商品價格:')
        a = list2[num].find('$')
        b = list2[num].find('</b>')
        priz.append('')
        #priz[num].append('')
        for i in range(a, b):
            priz[num] +=list2[num][i]
        print(priz)
        # 　print(num, i)
        # 　print(priz[num])
        # 　f.write('\n')


def main():
    N_list = []
    P_list = []
    f = open('momo.txt', 'w', encoding='utf-8')
    kw = input('請輸入商品名稱:')
    search(kw)
    gethtml(search(kw), N_list, P_list)
    writeinfo(N_list, P_list, f)
    f.close()


main()
from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data_csv():
    web_req = requests.get('http://notelections.online/region/region/st-petersburg?action=show&root=1&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217417&type=222')
    content = BeautifulSoup(web_req.text, 'html.parser')
    assets = content.select('table')
    url = 'http://notelections.online'
    current_data = []
    for i in range(1, len(assets[8].contents[1].contents)-2):
        web_req1 = requests.get(url + assets[8].contents[1].contents[i].contents[0].contents[0].attrs['href'])
        content1 =BeautifulSoup(web_req1.text, 'html.parser')
        assets1 = content1.select('tr')
        for j in range(1, len(assets1[32].contents)-2):
            myData = []
            myData.append(assets[8].contents[1].contents[i].text)

            for k in range(32, 44):
                myData.append(assets1[k].contents[j].text)

            for h in range(45, 48):
                s = assets1[h].contents[j].text
                lst = s.split()
                myData.append(lst[0])

            current_data.append(myData)

    df = pd.DataFrame(current_data)
    df.to_csv("data.csv", header=['ТИК', 'УИК', 'Число избирателей, внесенных в список избирателей на момент окончания голосования','Число избирательных бюллетеней, полученных участковой избирательной комиссией','Число избирательных бюллетеней, выданных избирателям в помещении для голосования в день голосования',
                                  'Число избирательных бюллетеней, выданных избирателям, проголосовавшим вне помещения для голосования',
                                  'Число погашенных избирательных бюллетеней','	Число избирательных бюллетеней, содержащихся в переносных ящиках для голосования',
                                  'Число избирательных бюллетеней, содержащихся в стационарных ящиках для голосования',
                                  'Число недействительных избирательных бюллетеней','Число действительных избирательных бюллетеней',
                                  '	Число утраченных избирательных бюллетеней','Число избирательных бюллетеней, не учтенных при получении',
                                  'Амосов Михаил Иванович','Беглов Александр Дмитриевич','Тихонова Надежда Геннадьевна'])

get_data_csv()
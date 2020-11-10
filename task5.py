import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    return pd.read_csv("data.csv").drop(columns="Unnamed: 0")

def get_turndata():
    return pd.read_csv("1.csv").drop(columns="Unnamed: 0")

'''df = get_data()
#явка
strs = df.values.tolist()
for str in strs:
        str.append((str[7]+str[8])/str[2])'''

#явка (сортировка по убыванию)
def turnout():
    df = get_data()
    strs = df.values.tolist()

    for str in strs:
        str.append((str[7]+str[8])/str[2])
    df = pd.DataFrame(strs)
    df.sort_values(16, ascending=False, inplace=True)
    df.to_csv('1.csv', header=['ТИК', 'УИК', 'Число избирателей, внесенных в список избирателей на момент окончания голосования','Число избирательных бюллетеней, полученных участковой избирательной комиссией','Число избирательных бюллетеней, выданных избирателям в помещении для голосования в день голосования',
                                  'Число избирательных бюллетеней, выданных избирателям, проголосовавшим вне помещения для голосования',
                                  'Число погашенных избирательных бюллетеней','	Число избирательных бюллетеней, содержащихся в переносных ящиках для голосования',
                                  'Число избирательных бюллетеней, содержащихся в стационарных ящиках для голосования',
                                  'Число недействительных избирательных бюллетеней','Число действительных избирательных бюллетеней',
                                  '	Число утраченных избирательных бюллетеней','Число избирательных бюллетеней, не учтенных при получении',
                                  'Амосов Михаил Иванович','Беглов Александр Дмитриевич','Тихонова Надежда Геннадьевна','Явка'])

#2
def candidate():
    df = get_data()
    strs = df.values.tolist()
    for str in strs:
        if (str[7]+str[8] > 100):
            str.append(str[14] / (str[7]+str[8]))
        else:
            str.append(0)
    df = pd.DataFrame(strs)
    df.sort_values(16, ascending=False, inplace=True)
    strs1 = df.values.tolist()
    current_data = []
    current_data.append(strs1[0])
    df = pd.DataFrame(current_data)
    df.to_csv('2.csv',
              header=['ТИК', 'УИК', 'Число избирателей, внесенных в список избирателей на момент окончания голосования',
                      'Число избирательных бюллетеней, полученных участковой избирательной комиссией',
                      'Число избирательных бюллетеней, выданных избирателям в помещении для голосования в день голосования',
                      'Число избирательных бюллетеней, выданных избирателям, проголосовавшим вне помещения для голосования',
                      'Число погашенных избирательных бюллетеней',
                      '	Число избирательных бюллетеней, содержащихся в переносных ящиках для голосования',
                      'Число избирательных бюллетеней, содержащихся в стационарных ящиках для голосования',
                      'Число недействительных избирательных бюллетеней',
                      'Число действительных избирательных бюллетеней',
                      '	Число утраченных избирательных бюллетеней',
                      'Число избирательных бюллетеней, не учтенных при получении',
                      'Амосов Михаил Иванович', 'Беглов Александр Дмитриевич', 'Тихонова Надежда Геннадьевна', 'Процент Беглова'])

#3
def difference():
    df = get_data()
    strs = df.values.tolist()

    for str in strs:
        str.append((str[7] + str[8]) / str[2])
    df = pd.DataFrame(strs)
    diff = df.groupby([0])[16].max() - df.groupby([0])[16].min()
    arr_n = diff.index.values.tolist()
    arr_ch = diff.values.tolist()
    current_data = []
    for i in range(len(arr_n)):
        arr = []
        arr.append(arr_n[i])
        arr.append(arr_ch[i])
        current_data.append(arr)
    for item in current_data:
        if max(arr_ch) == item[1]:
            print(item[0], item[1])

#4
def disp():
    df = get_data()
    strs = df.values.tolist()
    for str in strs:
        str.append((str[7] + str[8]) / str[2])
    df = pd.DataFrame(strs)
    diff = df.groupby([0])[16].var()
    arr_n = diff.index.values.tolist()
    arr_ch = diff.values.tolist()
    for i in range(len(arr_n)):
        print(arr_n[i], arr_ch[i], '\n')

#5 (посчитано для беглова, остальное аналогично)
def uik_number():
    df = get_data()
    strs = df.values.tolist()
    for str in strs:
        #str.append(str[13] / (str[7] + str[8]))
        str.append(str[14] / (str[7]+str[8]))
        #str.append(str[15] / (str[7] + str[8]))
    df = pd.DataFrame(strs)
    counts = df.groupby([16]).count()[1]
    arr_n = counts.index.values.tolist()
    arr_ch = counts.values.tolist()
    for i in range(len(arr_n)):
        print(arr_n[i], arr_ch[i], '\n')

def depend():
    df = get_data()
    strs = df.values.tolist()
    for str in strs:
        str.append((str[7]+str[8])/str[2])
        str.append(str[14] / (str[7] + str[8]))

    df = pd.DataFrame(strs)
    buf = df.loc[df[17] != -1].groupby([16])[17].mean()
    x = buf.index
    y = buf.values
    plt.figure(figsize=(16, 9))
    plt.scatter(x, y, alpha=0.4)
    plt.xlabel("Явка")
    plt.ylabel("Результат")
    plt.show()

turnout()
candidate()
difference()
disp()
uik_number()
depend()

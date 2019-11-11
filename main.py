import pandas as pd


def count_solution(num):
    data = []
    for i in range(1, 27):
        z = df.loc[:, [str(i)]]
        z_sum = z.loc[z.loc[:, str(i)] == num][str(i)].count()
        data.append(z_sum)
    return data


def percent_solution(arr):
    data = []
    for i in arr:
        data.append(i / 23 * 100)
    return data


if __name__ == '__main__':
    df = pd.read_csv('monitoring_9.csv')
    pd.set_option('display.max_columns', None)
    pd.set_option('max_colwidth', 15)
    pd.set_option('display.width', 115)
    print(df)

    print('--------|{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}'.format(*[i for i in range(1, 27)]))       

    print('Верно   |', end='')
    a = count_solution(1)
    print('{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}'.format(*a))
    a_p = percent_solution(a)
    print('Верно % |{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}'.format(*a_p))

    print('Неверно |', end='')
    b = count_solution(0)
    print('{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}'.format(*b))
    b_p = percent_solution(b)
    print('Неверно%|{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}{:4.0f}'.format(*b_p))

    odf = pd.DataFrame(data={"Верно": a, "Верно, %": a_p, "Неверно": b, "Неверно, %": b_p})
    odf.to_csv("./file.csv", sep=',',index=False)
    
    idf = pd.read_csv('file.csv')
    print(idf)
    
    list_alg = list(df)
    
    for i in range(15, 20):
        list_alg.remove(list_alg[i])
    print(list_alg)
    
    list_geom = list(df)
    print(list_geom)
    for i in range(2, 15):
        list_geom.remove(list_geom[i])


    df['Всего'] = df.sum(axis=1)
    df['Алгебра'] = df[list_alg].sum(axis=1)
    df['Геометрия'] = df[list_geom].sum(axis=1)

    print(df)

# !/usr/bin/python3
# encoding: utf-8

import os
import pandas as pd

'''
Version 0.4

Имеем эталонную матрицу main, и secondary матрицу в которой нужно отсортировать столбцы по шаблону(main)
'''
#Включить/выключить интерактивный режим. Включть конечно, круть, остается только циферки нажимать... Правда-правда...
#Если выключить интерактивный режим, то файлы потребуется прописать вручную, см. строку 54
interactive_mod = 'y'
#Удалять пустые столбцы или не удалять)) скрипт смотрит только на заголовок, поэтому если в столбце что-то есть, а заголовок пустой то он подлежит экстерминатусу)...
unnamed_del = 'n'


if interactive_mod == 'y':
    temp_files = list(os.listdir())
    #temp_files = list(temp_files)
    files = {}
    for row in temp_files:
        if row.endswith('.csv') or row.endswith('.xlsx') or row.endswith('.xls'):
            files[row] = row

    files = dict(enumerate(files))
    for row in files:
        print(row, ' - ', files[row])

    input_main = input("Напишите 'exit' если вам нужно покинуть сие творение \nEnter a number reference file - main file:")
    if input_main == 'exit':
        print('Quit script')
        raise SystemExit()
    elif int(input_main) > (max(files)):
        print('You input too large number')
        raise SystemExit()
    else:
        input_main = files[int(input_main)]
    print('You selected a input_main >', input_main)

    input_secondary = input("Напишите 'exit' если вам нужно покинуть сие творение \nEnter a number the file in which you want to mix columns - secondary file: ")
    if input_secondary == 'exit':
        print('Quit script')
        raise SystemExit()
    elif int(input_secondary) > len(files):
        print('You input too large number')
        raise SystemExit()
    else:
        input_secondary = files[int(input_secondary)]
    print('Your selected a input_secondary >', input_secondary)
else:
    '''
    Если отключен интерактивный режим, то следует обрабатываемые файлы прописать в ручную
    '''
    #Эталонный файл, по которому будем равнятся
    input_main = '1.16_MTA.xlsx'
    #Файл что нам нужно перемешать
    input_secondary = '10.1_LSE.csv'

output = 'upd_' + input_secondary

#проверяем формат input_main файла
if input_main.endswith('.xls'):
    main = pd.read_excel(input_main).columns.tolist()
elif input_main.endswith('.csv'):
    try:
        main = pd.read_csv(input_main, sep=',', encoding="UTF-8").columns.tolist()
    except Exception as ex:
        main = pd.read_csv(input_main, sep=',', encoding="cp1251", low_memory=False).columns.tolist()
else:
    print('Неверный формат input_main файла')

#проверяем формат input_secondary файла
if input_secondary.endswith('.xls'):
    secondary = pd.read_excel(input_secondary)
elif input_secondary.endswith('.csv'):
    try:
        secondary = pd.read_csv(input_secondary)
    except Exception as ex:
        secondary = pd.read_csv(input_secondary, sep=',', encoding='cp1251', low_memory=False)
else:
    print('Неверный формат input_secondary файла')

temp = secondary.reindex(columns=main)

#применяем магию и получаем отсортированный документ
for n in main:
    for i in secondary:
        if n != i:
            temp[i] = secondary[i].values.tolist()

#Фиговая магия, пометила пустые столбцы как Unnamed. - удаляем название или целиком столбцы - зависит от настройки unnamed_del
if unnamed_del == 'n':
    temp.columns = temp.columns.str.replace('Unnamed.*', '')
elif unnamed_del == 'y':
    print(temp.filter(regex='Unnamed*'))
    temp = temp.drop(temp.filter(regex='Unnamed*').columns, axis=1)
else:
    print('unnamed_del - значение задано неверно')


temp.to_csv(output, sep=',', index=False)

print('Script complete')

# -*- coding: utf-8 -*-
# !/usr/bin/python3

'''
Пробегаемся по папкам и если встречаем триггер файл (delete_logs.py),
то удаляем все (файлы и папки) в папке с ним.

'''

import os
import shutil

# значение исходной папки для рекурсивного сканирования
dir = os.path.expanduser('/home/anatoly.bobunov/SF_Co')


def delete_logs(folder_dir):
    '''
    На входе получаем адрес папки с триггерным файлом.
    Удаляем в папке все файлы и папки, кроме тех что оканчиваются на '.py','.py~','.idea'
    доп фильтр можно добавить по собственному желанию
    '''
    for filename in os.listdir(folder_dir):
        if filename.endswith(('.py', '.py~', '.idea')) is False:
            file = os.path.join(folder_dir, filename)
            try:
                if os.path.isfile(file):
                    print(file + 'DELETED')
                    os.unlink(file)
                elif os.path.isdir(file):
                    print(file + ' DELETED')
                    shutil.rmtree(file)
            except Exception as e:
                print(e)


filelist = list(os.walk(dir))

for root, dirs, files in filelist:
    '''
    Пробегает по всем подпапкам, если находим delete_log.py
    то возвращаем полный путь до этой папки
    '''
    for name in files:
        if name == 'delete_logs.py':
            folder_dir = os.path.join(root)
            delete_logs(folder_dir)


print('Delete is completed')

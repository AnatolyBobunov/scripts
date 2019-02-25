# -*- coding: utf-8 -*-
#!/usr/bin/env python
import csv
import string
import os
file_log=open("log.html","w") #открываем html лог файл
file_log_all=open("log_all.txt","w") #открываем txt лог файл
config_file = open('config.csv')#открываем конфиг файл 
config = csv.reader(config_file, delimiter=',')#считываем конфиг файл 
config=[line for line in config]#итерируем что бы получить список вложенных списков из конфиг файла
config_file.close()

files= [f for f in os.listdir(os.getcwd()+"/Ishodn/") if (os.path.isfile(os.path.join(os.getcwd()+"/Ishodn/", f))) and f.endswith(".csv") ] #получаем список всех csv файлов в папке ishodn
for file in files:
	i=0 #переменная для проверки былал ли замена
	print("Open this csv file "+str(file))
	file_log_all.write("\nOpen this csv file "+str(file)+"\n")
	file_ishodn=open(os.getcwd()+"/Ishodn/"+file,"r")
	file_zamen=open(os.getcwd()+"/Replaced/"+file,"w")
	for line in file_ishodn: #построчно читаем csv в котором заменяем
		for line_config in config: #получаем вложенные списки из 2х элементов
			a,b=line_config #присваиваем a-что меняем b- на что меняем
			if a in line:
				line=line.replace(","+a+",",","+b+",") # заменяем в строке a на b
				i=i+1 #
				file_log_all.write("    Line "+str(i)+" Replace "+a+"  to  "+b+"\n")
		file_zamen.write(line)
	if i!=0:
		file_log.write(str(file)+"<font color=\"red\"> is CHANGE</font></br>")
	else:
		file_log.write(str(file)+"<font color=\"green\"> is NOT CHANGE</font></br>")	
	file_ishodn.close()
	file_zamen.close()
file_log.close()
file_log_all.close()
#input("Done")

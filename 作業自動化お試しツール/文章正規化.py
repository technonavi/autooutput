from bs4 import BeautifulSoup
import requests
import re
import csv
def readtxt():
 f = open('scraping.txt', 'r', encoding='UTF-8')
 read_txt = f.read()
 f.close()
 return read_txt
d=readtxt()
print(d)
company = re.findall('有限.*' , d)
person = re.findall('.*様' , d)
department = re.findall('株式.*部' , d)
print("会社名:",company[0])
print("人物:",person[0])
print("開発部",department[0])






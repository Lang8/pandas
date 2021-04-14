from bs4 import BeautifulSoup

file_name = '2021_01.html'
soup = BeautifulSoup(open('output/{}'.format(file_name),encoding='UTF-8'),'html.parser')

print(soup.find_all("thead"))

# bscontroller = BeautifulSoup
from selenium import webdriver
from parse import compile
import os,time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
p = compile('{}<table{}</table>{}<table{}</table>{}<table{}</table>{}<table{}</table>{}<table{}</table>{}<table{}</table>{}<table{}</table>{}<table{}</table>{}')
# chrome 과 Driver 모두 89버전
driver = webdriver.Chrome(os.path.join(BASE_DIR,'chromedriver.exe'))

driver.implicitly_wait(3)
driver.get('http://portal.kleague.com/user/loginById.do?portalGuest=rstNE9zxjdkUC9kbUA08XQ==')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/ul/li/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="contentsLayer"]/div/div/ul/li[3]/a').click()
time.sleep(1)
''' select box value '''
year = 2021
league = 1
sinceRound = 1 # game 1~6 -> round 1 ==> round = 1 + (game-1)/6 
untilRound = 9
untilRound *= 6

for game in range(sinceRound,2):
    driver.find_element_by_xpath("//select[@name='meetYear']/option[@value={}]".format(year)).click()
    driver.find_element_by_xpath("//select[@name='meetSeq']/option[@value={}]".format(league)).click()
    driver.find_element_by_xpath("//select[@name='roundId']/option[@value={}]".format(1+(game-1)//6)).click()
    driver.find_element_by_xpath("//select[@name='gameId']/option[@value={}]".format(game)).click()

    html = driver.page_source
    pattern = p.parse(html)
    
    with open("foo.txt","w+", encoding="UTF-8") as f:
        for idx,item in enumerate(pattern,0):
            if(idx % 2):
                print(idx)
                f.write('<table ')
                f.write(item)
                f.write('</table>')
                f.write('\n')
# time.sleep(5)
driver.quit()
from bs4 import BeautifulSoup
import pandas as pd, xlsxwriter
import os

preloadRow = [['번호', '선수', '포지션', '출전시간', '평점', '득점', '도움', '슈팅', '유효슈팅', '블락된 슈팅', '벗어난 슈팅', 'PA내슈팅', 'PA외슈팅', '오프사이드', '프리킥', '코너킥', '스로인', '드리블 성공', '드리블 성공률(%)'],
['번호', '선수', '포지션', '출전시간', '평점', '패스 성공', '패스 성공률(%)', '키패스', '공격진영패스 성공', '공격진영패스 성공률(%)', '중앙지역패스 성공', '중앙지역패스 성공률(%)', '수비진영패스 성공', '수비진영패스 성공률(%)', '롱패스 성공', '롱패스 성공률(%)', '중거리패스 성공', '중거리패스 성공률(%)', '숏패스 성공', '숏패스 성공률(%)', '전진패스 성공', '전진패스 성공률(%)', '횡패스 성공', '횡패스 성공률(%)', '백패스 성공', '백패스 성공률(%)', '크로스 성공', '크로스 성공률(%)', '탈압박'], 
['번호', '선수', '포지션', '출전시간', '평점', '경합(지상) 성공', '경합(지상) 성공률(%)', '경합(공중) 성공', '경합(공중) 성공률(%)', '태클 성공', '태클 성공률(%)', '클리어링', '인터셉트', '차단', '획득', '블락', '볼미스', '파울', '피파울', '경고', '퇴장'], 
['번호', '선수', '포지션', '출전시간', '평점', '실점', '캐칭', '펀칭', '골킥 성공', '골킥 성공률(%)', '공중볼 처리 성공', '공중볼 처리 성공률(%)']] 
sheet_name_list = ['home_Att','away_Att','home_PS','away_PS','home_Def','away_Def','home_GK','away_GK']

file_list = os.listdir('./output/')
file_names = [file for file in file_list if file.endswith('.html')]

print(file_names)

for file_name in file_names:
    print('file open {}'.format(file_name))
    soup = BeautifulSoup(open('output/{}'.format(file_name),encoding='UTF-8'),'html.parser')
    tables = soup.find_all("table")
    rs = []
    for idx, table in enumerate(tables,0):
        rows = [preloadRow[idx//2]]
        trs = table.find_all("tr")
        for i, tr in enumerate(trs,0):
            row = []
            if i < 2: # line replace pre-loaded
                i += 1
                continue
            tds = tr.find_all("td")
            for td in tds:
                row.append(td.string)
            rows.append(row)
        rs.append(rows)
    with pd.ExcelWriter('./result/{}'.format(file_name.replace('html','xlsx')),engine='xlsxwriter') as writer:
        for idx, r in enumerate(rs,0):
            pr = pd.DataFrame(r)
            pr.to_excel(writer, sheet_name=sheet_name_list[idx])
    
# bscontroller = BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd, xlsxwriter


file_name = '2021_01'
soup = BeautifulSoup(open('output/{}.html'.format(file_name),encoding='UTF-8'),'html.parser')

preloadRow = [[['번호', '선수', '포지션', '출전시간', '평점', '득점', '도움', '슈팅', '유효슈팅', '블락된 슈팅', '벗어난 슈팅', 'PA내슈팅', 'PA외슈팅', '오프사이드', '프리킥', '코너킥', '스로인', '드리블', '드리블'],
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '성공', '성공률(%)']],
[['번호', '선수', '포지션', '출전시간', '평점', '패스', '패스', '키패스', '공격진영패스', '공격진영패스', '중앙지역패스', '중앙지역패스', '수비진영패스', '수비진영패스', '롱패스', '롱패스', '중거리패스', '중거리패스', '숏패스', '숏패스', '전진패스', '전진패스', '횡패스', '횡패스', '백패스', '백패스', '크로스', '크로스', '탈압박'], 
['','','','','','성공', '%','', '성공', '%', '성공', '%', '성공', '%', '성공', '%', '성공', '%', '성공', '%', '성공', '%', '성공', '%', '성공', '%', '성공', '%', '']],
[['번호', '선수', '포지션', '출전시간', '평점', '경합(지상)', '경합(지상)', '경합(공중)', '경합(공중)', '태클', '태클', '클리어링', '인터셉트', '차단', '획득', '블락', '볼미스', '파울', '피파울', '경고', '퇴장'], 
['','','','','','성공', '성공률(%)', '성공', '성공률(%)', '성공', '성공률(%)','','','','','','','','','','']],
[['번호', '선수', '포지션', '출전시간', '평점', '실점', '캐칭', '펀칭', '골킥', '골킥', '공중볼 처리', '공중볼 처리'], 
['','','','','','','','','성공', '성공률(%)', '성공', '성공률(%)']]]
sheet_name_list = ['home_Att','away_Att','home_PS','away_PS','home_Def','away_Def','home_GK','away_GK']
tables = soup.find_all("table")
writer = pd.ExcelWriter('{}.xlsx'.format(file_name),engine='xlsxwriter')
for idx, table in enumerate(tables,0):
    rows = []
    trs = table.find_all("tr")
    for i, tr in enumerate(trs,0):
        row = []
        if i < 2:
            # line replace pre-loaded
            rows.append(preloadRow[idx//2][i])
            i += 1
            continue
        # ths = tr.find_all("th")
        # if ths != []:
        #     for th in ths:
        #         row.append(th.string)
        tds = tr.find_all("td")
        for td in tds:
            row.append(td.string)
        rows.append(row)
    rs = pd.DataFrame(rows)
    rs.to_excel(writer, sheet_name=sheet_name_list[idx])
writer.save()
    
# bscontroller = BeautifulSoup
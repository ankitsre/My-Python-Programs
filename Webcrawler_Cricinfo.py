
###This a simple webcrawler to crawl data from cricinfo website. Selenium has been used to connect to webpage. Beuatifulsoup has used to parse html content


#####configuring the drivers and finding out the relevant tags
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
driver  = webdriver.Chrome('C:/Users/subha/Downloads/chromedriver_win32 (1)/chromedriver.exe')
driver.get('http:\\www.stats.espncricinfo.com/ci/content/records/283683.html')
text1 = driver.page_source
soup1 = bs(text1, 'html.parser')
text = soup1.find('div', attrs= {'id' : 'ciHomeContentlhs'} )


########data parsing for relevant fields
head = []
for a in text.findAll('th'):
    head.append(a.text)
    
Player, Span, Mat, Runs, HS, Ave_Bat, Centuries, Wkts, BBI, Ave_Bowl, Five_W_Hauls, Ct, St = [],[],[],[],[],[],[],[],[],[],[],[],[]

for a in text.findAll('tr' , attrs = {'class':'data1'}):
    player= a.findAll('td')[0].text
    span= a.findAll('td')[1].text
    mat = a.findAll('td')[2].text
    runs = a.findAll('td')[3].text
    hs = a.findAll('td')[4].text
    ave = a.findAll('td')[5].text
    cen = a.findAll('td')[6].text
    wkt = a.findAll('td')[7].text
    bbi = a.findAll('td')[8].text
    av = a.findAll('td')[9].text
    fi = a.findAll('td')[10].text
    ct = a.findAll('td')[11].text
    st = a.findAll('td')[12].text
    Player.append(player)
    Span.append(span)
    Mat.append(mat)
    Runs.append(runs)
    HS.append(hs)
    Ave_Bat.append(ave)
    Centuries.append(cen)
    Wkts.append(wkt)
    BBI.append(bbi)
    Ave_Bowl.append(av)
    Five_W_Hauls.append(fi)
    Ct.append(ct)
    St.append(st)
    
data = pd.DataFrame(zip(Player, Span, Mat, Runs, HS, Ave_Bat, Centuries, Wkts, BBI, Ave_Bowl, Five_W_Hauls, Ct, St) , columns = head)

data.to_excel('Players_Test.xlsx' , index = False)

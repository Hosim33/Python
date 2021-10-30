import urllib.request
from bs4 import BeautifulSoup

web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup = BeautifulSoup(web, 'html.parser')
tmp=soup.select('li')
print("*** 서울여자대학교 학과 및 홈페이지 ***")
print("학과                  홈페이지")
for i in tmp[:-3]:
    if i.text=="공동기기실" or i.text=="컴퓨터학과(*)" or i.text=="콘텐츠디자인학과(*)":
        continue
    print(i.text,end="          ")
    web2=urllib.request.urlopen('http://www.swu.ac.kr'+i.select_one("a")["href"])
    soup2=BeautifulSoup(web2,'html.parser')
    tmp2=soup2.find("a", {'class':"btn btn_xl btn_blue_gray"})
    if tmp2.text=="홈페이지바로가기" or tmp2.text=="홈페이지 바로가기":
        print(tmp2['href'])
    else:
        print("홈페이지가 존재하지 않음")




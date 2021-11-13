import urllib.request
from bs4 import BeautifulSoup
import os

opener=urllib.request.build_opener()   #오프너 객체 생성 후 헤더 추가
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1;) WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

//크롤링할 웹툰 지정
webtoon = urllib.request.urlopen('https://comic.naver.com/webtoon/list?titleId=735078')
soup = BeautifulSoup(webtoon, 'html.parser')
toontitle = soup.find("div",{"class": "detail"}).find("h2").text.split()[0] #웹툰 제목으로 폴더 생성

os.mkdir(toontitle)
os.chdir(toontitle)

tmp=soup.findAll('td',{"class":"title"}) 

for j in tmp:
    os.mkdir((j.text).strip()) #회차로 폴더 생성
    os.chdir((j.text).strip())

    tmp2=urllib.request.urlopen("https://comic.naver.com" + j.a['href']) #회차별 사이트 정보 가져오기
    tmp2_r=BeautifulSoup(tmp2, 'html.parser')
    
    photo = tmp2_r.find("div",{"class", "wt_viewer"})
    photo_save = photo.findAll("img")
    
    index=1
    for i in photo_save:
        urllib.request.urlretrieve(i['src'], str(index)+".jpg") #이미지 저장
        index+=1

    os.chdir("..") #다음 회차 저장을 위해 이전 폴더 이동

from selenium import webdriver
import time

path= "C:/Temp/chromedriver.exe"
driver=webdriver.Chrome(path)  #드라이버 경로

driver.get("http://zzzscore.com/1to50/")  #게임 사이트 접속하기
btn=driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')  #클릭할 버튼의 xpath 1~25까지 전부 받기

num=1  #1~50까지 숫자를 비교할 때 사용할 변수

while(num<=50):  #50까지 클릭하도록 하는 반복문
    for i in btn:
        if i.text == str(num): #btn의 text값이 num 값과 같을 때 실행
            print(str(num) + " 클릭")  #숫자 클릭 출력
            i.click()  #클릭
            num +=1  #num 값 증가

    

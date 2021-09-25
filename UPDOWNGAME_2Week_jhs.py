'''UP&DOWN GAME  제작자 : SWING 28th jhs'''
import datetime
import os          #게임기록 파일이 현재경로에 존재하는지 확인하기 위함
d=datetime.datetime.now()
import random       #답을 랜덤으로 지정하기 위한 import
count= player= min_n = 1   #player가 입력하는 수 player와 입력받은 횟수 count, min_n은 숫자 범위 축소를 위해 가장 작은 수
max_n = 100  #숫자 범위 축소를 위해 가장 큰 수
score = {}  #기록확인을 위해 닉네임과 count를 저장할 딕셔너리 선언, key는 count value는 닉네임
while(1):  #무한루프로 게임을 종료하기 전까지 돌린다.
    answer = random.randrange(1,101)  #정답 수를 random.randrange로 1부터 100 사이의 한 수로 지정
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    num=int(input(">>"))        #num은 메뉴 1~3 중에 입력받는다.
    if num ==1:     #게임시작
        while(count <= 10):    #최대기회가 10번이므로 count가 10 이하일 때까지 반복문
            while(1):
                player=int(input("%d번째 숫자 입력(%d~%d) : " %(count,min_n,max_n)))  #player 변수에 수를 입력받는다.
                try:      #2번 피드백
                    if player < 1 or player > 100:          #1~100 사이의 수가 아닐 경우 raise로 오류를 발생시켰다.
                        raise
                except:
                    print("1~100 사이의 수만 가능합니다. 다시 입력해주세요.")
                else:
                    break
            if player == answer:     #정답일 경우
                print("정답입니다!!")
                print("%d번째만에 맞추셨습니다" %count)
                if not score or list(score.keys())[0] > count:    #현재 count 값이 score 딕셔너리의 키 리스트에서 0번 인덱스보다 작을 경우 최고기록이다.
                    print("최고기록 갱신~!")       #3번 피드백      아직 오늘의 기록이 없을 수도 있기 때문에 score 값을 if not 으로 확인해준다. 
                    score[count]=input("닉네임을 입력하세요 >> ")    #닉네임을 score 딕셔너리의 value에 count는 key값으로 저장해준다. 
                sorted(score)   #key값을 기준으로 오름차순 정렬한다.
                count = min_n = 1  #count랑 min_n 리셋
                max_n = 100    #max_n도 리셋
                break   #정답 맞춘 게임을 탈출하고 다음판 시작
            elif player < answer:   #입력한 수가 정답보다 작을 경우
                count+=1    
                print("UP")
                if min_n < player:      #1번 피드백
                    min_n=player+1     #min_n값을 바꿔주면서 출력되는 숫자 범위 변경
            else:        #입력한 수가 정답보다 클 경우
                count+=1
                print("DOWN")
                if max_n > player:     #1번 피드백
                    max_n=player-1     #max_n값을 바꿔주면서 출력되는 숫자 범위 변경
    elif num ==2:        #기록확인
        if(os.path.isfile('record.txt')):         #record.txt 파일이 있는지 검증을 통해 있으면 파일을 읽어와서 출력해준다.
            f=open('record.txt','r')
            lines = f.readlines()
            for index, line in enumerate(lines):
                print(index+1, line,end="")
            f.close()
        else:            #record.txt 파일이 없는 경우에는 현재 딕셔너리에 있는 값들을 리스트로 변환하여 인덱스와 함께 출력해준다.
            val=list(score.values())
            date = d.strftime("%Y-%m-%d\n")
            for index, key in enumerate(list(score)):
                print(index+1, key, val[index], date)
        #for index, value in enumerate(score):    #score 리스트의 값을 인덱스와 함께 출력한다.
            #print(index+1, value)   #인덱스에 1을 더해서 1등부터 나올 수 있게 했다.
    else:      #게임종료
        print("UP & DOWN 게임이 종료됩니다.")
        date = d.strftime("%Y-%m-%d\n")
        f=open('record.txt','a')          #게임을 종료할 때 record.txt 파일에 기록을 써준다.
        for key, value in score.items():           
            f.write(value + " ")
            f.write(str(key) + " ")
            f.write(date)
        f.close()
        break       #무한루프 탈출로 게임을 완전히 종료

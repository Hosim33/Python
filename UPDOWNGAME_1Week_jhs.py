'''UP&DOWN GAME  제작자 : SWING 28th jhs'''
import random       #답을 랜덤으로 지정하기 위한 import
count= player= min_n = 1   #player가 입력하는 수 player와 입력받은 횟수 count, min_n은 숫자 범위 축소를 위해 가장 작은 수
max_n = 100  #숫자 범위 축소를 위해 가장 큰 수
score = []  #기록확인 기능을 위해 빈 리스트 선언
while(1):  #무한루프로 게임을 종료하기 전까지 돌린다.
    answer = random.randrange(1,101)  #정답 수를 random.randrange로 1부터 100 사이의 한 수로 지정
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    num=int(input(">>"))        #num은 메뉴 1~3 중에 입력받는다.
    if num ==1:     #게임시작
        while(count <= 10):    #최대기회가 10번이므로 count가 10 이하일 때까지 반복문
            player=int(input("%d번째 숫자 입력(%d~%d) : " %(count,min_n,max_n)))  #player 변수에 수를 입력받는다.
            if player == answer:     #정답일 경우
                score.append(count)   #기록확인용 리스트 score에 count 값을 추가한다.
                print("정답입니다!!")
                print("%d번째만에 맞추셨습니다" %count)
                if score[0] >= count:    #현재 count 값이 score 리스트의 0번 인덱스보다 작을 경우 최고기록이다.
                    print("최고기록 갱신~!")
                score.sort()   #score 리스트를 정렬한다.
                count = min_n = 1  #count랑 min_n 리셋
                max_n = 100    #max_n도 리셋
                break   #정답 맞춘 게임을 탈출하고 다음판 시작
            elif player < answer:   #입력한 수가 정답보다 작을 경우
                count+=1    
                print("UP") 
                min_n=player+1     #min_n값을 바꿔주면서 출력되는 숫자 범위 변경
            else:        #입력한 수가 정답보다 클 경우
                count+=1
                print("DOWN")
                max_n=player-1     #max_n값을 바꿔주면서 출력되는 숫자 범위 변경
    elif num ==2:        #기록확인
        for index, value in enumerate(score):    #score 리스트의 값을 인덱스와 함께 출력한다.
            print(index+1, value)   #인덱스에 1을 더해서 1등부터 나올 수 있게 했다.
    elif num ==3:        #게임종료
        print("게임을 종료합니다.") 
        break       #무한루프 탈출로 게임을 완전히 종료

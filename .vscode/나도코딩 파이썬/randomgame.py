
#소수점 제거 후 랜덤값 0~100
#print(round(random()*100))
#print(int(random()*100))

#범위 랜덤값 1이상 100미만
#print(randrange(1, 100))
#범위 랜덤값 1이상 100이하
#print(randint(1, 100))

#ver_12_28

from random import *
import time
import os

level = 0
stop =  False
print("\n\n==============================")
print("🗡 장비 강화 시스템을 시작합니다!🗡")
print("==============================")
ask = input("장비 강화를 하시겠습니까?🐱‍👤 (Y/N 을 입력하세요): ")
print("==============================")
if ask == "Y" or ask == "y" :
    while stop == False :
        print("강화 중 입니다...(MAX 7강)")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")
        gamble = randint(1,100)
        if 10 >= gamble > 0  and level > 0:
            print("==============================")
            print("장비가 파괴되었습니다 ㅠㅠ");
            print("==============================")
            level = 0
            ask2 = input("\n\n새 장비🗡 를 준비했습니다. \n계속 강화 하시겠습니까?🤭(Y/N): ")
            if ask2 == "N" or ask2 == "n" :
                print("\n당신은 쫄보입니다😜 \n")
                time.sleep(3)
                stop = True
        elif 50>= gamble > 10 and level > 0 :
            print("==============================")
            print("강화가 실패했습니다!!!😒");
            print("==============================")
            level -= 1
            ask2 = input("\n\n계속 강화 하시겠습니까?🤭 (Y/N): ")
            if ask2 == "N" or ask2 == "n" :
                print("\n당신은 쫄보입니다😜 \n")
                time.sleep(3)
                stop = True
        else :
            print("장비가 강화되었습니다!!!")
            print("==============================")
            level += 1
            print("현재 장비의 레벨은 +%d강 입니다."%level)
            print("==============================")
            if level == 7 :
                print("\n장비가 최대로 강화되었습니다!! 축하합니다🏆 \n")
                stop = True
            else :
                ask2 = input("\n\n계속 강화 하시겠습니까?🤭 (Y/N): ")
        if ask2 == "N" or ask2 == "n" :
            print("\n당신은 쫄보입니다😜 \n")
            time.sleep(3)
            stop = True
else :
    print("\n당신은 쫄보입니다😜 \n")
    time.sleep(3)
    
from math import pi

radius = float(input("반지름을 입력하세요: "))
area = ((radius ** 2) * pi)
print ("반지름" + str(radius) + "의 원넓이는" + str(area) + "입니다.")
#print ("반지름", radius,"의","원넓이는", area ,"입니다.")

# 출력문 주석된것과 아닌것의 차이가 궁금합니다.
# 주석 아닌것은 str 을 붙이지 않으면 에러가 납니다.
# 결론) 연산으로 들어가서 문자열이 계산불가
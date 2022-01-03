age = 4;
is_adult =  age >= 3;

print (is_adult);
print (age);

languages = ['python', 'perl', 'c', 'java', 'c#']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")

#quiz 1

#station1 = "사당"  
#station2 = "신도림"
#station3 = "인천공항"

station = ["사당", "신도림", "인천공항" ] 

for i in station:
    print(i + " 행 열차가 들어오고 있습니다.") 

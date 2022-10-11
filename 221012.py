dic = {"jg":"준경","hs":"희성"}
print(dic)
del dic["hs"]
print(dic)
dic = {"num":3}
print(dic)



dic = {"hs":"희성", "jg":"준경", "ja":"진암"}
print(dic.keys())
names = list(dic.keys())
print(names)
names.append("현우")
print("새로운 리스트", names)
print("원레 dic key", list(dic.keys()))
print("k v", dic.items())




areadata = {'서울시':57, '부산시':62, '대구시':59, 
            '인천시':59, '강화군':58, '서해5도' : 64, 
            '광주시' :62, '대전시':60, '울산시':53, 
            '세종시':58	}

report = {'위험': '설사, 구토 등 식중독 의심 증상이 있으면 의료기관을 방문하여 의사 지시에 따름',
         '경고': '조리도구는 세척, 소독 등을 거쳐 세균오염을 방지하고 유통기한, 보관방법 등을 확인하여 음식물 조리. 보관에 각별히 주의하여야 함',
         '주의': '조리음식은 중심부까지 75℃(어패류 85℃)로 1분 이상 완전히 익히고 외부로 운반할 때에는 가급적 아이스박스 등을 이용하여 10℃이하에서 보관 및 운반',
         '관심': '화장실 사용 후, 귀가 후, 조리 전에 손 씻기를 생활화'
         }
show = {}
for key, value in areadata.items() :
  if value >= 86 :check = '위험'
  elif value >= 71 :check = '위험'
  elif value >= 55 :check = '위험'
  else : check = '위험'
  show[key] = check
  print(show)
city = input("도시 입력해 : ")
print(f'\n\n{city} : {areadata[city]}, {show[city]}\n{report[show[city]]}')


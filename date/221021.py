
a = [1,2,4,3]
# print(sorted(a)) 반환값 정렬된 배열
# print(a.sort()) 반환값 none
# print(a.reverse()) 반환값 none
# print(reversed(a)) 반환값 X

# a.reverse() 직접적인 영향을 줌
# print(a)

# a.sort() 직접적인 영향을 줌
# print(a)

# b = list(reversed(a)) a에는 영향을 안 줌 list로 묶어줘야함 아니면 에러
# print(b)
# print(a)

# b = sorted(a) 안 묶어도 되고 a에는 영향을 안 줌
# print(b)
# print(a)

# print(list(reversed(a))) print 안에 넣으려면 이렇게 a에는 영향을 안 줌
# print(a)

# print(sorted(a)) 그냥 넣을 수 있고 a에 영향을 안 줌
# print(a)
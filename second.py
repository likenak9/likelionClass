# a = int(input("input number! : "))
# 
# if (a == 10):
#     print("a is 10")
# else:
#     print("a is not 10")
#     

# if (a > 0):
#     print("a is sang")
#     if (a%2==0):
#         print("a is jjak")
#     else:
#         print("a is hol")
# else:
#     print("a is m# inus")
#     

#########
# i = 1
# while i < 1000:
#     print(i)
#     i = i +1
#     
#    i += 1 위의 줄을 대신하는 간소화 문법
# ctrl + c 는 파이선 문법 실행 취소
# tmp_str = "오늘은 토요일오후수업시간입니다."
# print(len(tmp_str))
# print(range(len(tmp_str)))
# print((tmp_str[1]))
# 
# def forfunction(a):
#     for i in range(a):
#         print(i)
# forfunction(100)


def mysum(a,b):
    c = a * b
    return c

    
print(mysum(3,5))

def mygugu(a):
    print(a,"단 입니다.")
    for i in range(1,10):
        c = a * i
        print(a," 곱하기 ",i,"        ",c)
        
mygugu(9)

# class NS5:
#     body = "power"
#     
#     def run(self):
#         print("run")
# 
# NS5
        

    
# for i in range(1000):
#     print("i의 값은 ",i)
# 
# i = 1
# while i < 5:
#     print("i의 값은 ",i)
#     i = i +1
#     # 
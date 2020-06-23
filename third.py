#6/23 class
# def endwords(a):
#     word1 = a
#     
# 
word1 = input("끝말잇기를 시작합시다 : ")

if len(word1) == 3:
    pre_word = word1
    print(pre_word[-1] + "로 시작되는 단어를 입력하세요.")
    while True:
        word2 = input()
    
        if (len(word2) == 3) and (word2[0] == pre_word[-1]):
            print("정답입니다." + word2[-1] + "로 시작되는 단어를 입력하세요.")
            pre_word = word2
        else:
            print("오답입니다.")
            break
        
else:
    print("3글자만 가능합니다.")

    
# def endwords(a):
#     word1 = input("단어를 입력하세요. : ", a)
#     print(a)
#     
# endwords
# 깃 허브에서 수정중입니다.



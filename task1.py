# Напишите программу, которая получает на вход две строки, и формирует из них словарь. 
# Ключами служат слова из первой строки, значениями – целые числа из второй.
# Пример ввода
# яблоки сливы груши персики манго киви апельсины
# 34 56 23 89 55 32 11
masiv_slov = list(map(str, input().split()))
massiv_ch = list(map(int, input().split()))


dic = {}

for i in range(len(masiv_slov)):
    dic[masiv_slov[i]] = massiv_ch[i]

print(dic)
# Напишите программу, которая получает на вход строку чисел, разделенных пробелами, и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".
n = list(map(str, input().split()))



dic = {}

for i in range(len(n)):
    if int(n[i]) % 2 == 0:
        dic[n[i]] = "Четное"
    else:
        dic[n[i]] = "Нечетное"

print(dic)
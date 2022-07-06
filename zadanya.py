# from random import choice,randint
# #1
# a=int(input())
# b=int(input())
# if a % 2:
#     a += 1
# print(" ".join(str(i) for i in range(a, b + 1, 2)))
# #2
# t = ['Сколько месяцев в году имеют 28 дней?',
#              'Что в огне не горит и в воде не тонет?',
#              'Кого австралийцы называют морской осой?']
# q_f = ['все', 'лёд', 'медузу']
# g=randint(0,2)
# q = q_f[g]
#
# re=choice(t)
# print(re)
# aq=input()
# if aq == q:
#     print('правильно')
# else:
#     print( 'неправильно ХИ-ХИ-ХИ-ХА')
#3 1860
summ=int(input("сумма  "))
proc=int(input('процент  '))
for ie in range(5):
   summ=summ+summ*(proc/100)
print(summ)
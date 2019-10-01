# html出力
print('''<h1>paizaラーニング入門編</h1>''')

# random出力
import random
number = random.randint(1,100)    #1〜100の範囲で抽選
print('ランダム抽選の結果は'+str(number))


# if文による条件分岐
# おみくじプログラム
import random
omikuji = random.randint(1,10)
#print(omikuji)

if omikuji == 1:
    print('大吉')
elif omikuji == 2:
    print('中吉')
elif omikuji <= 4: #3,4
    print('小吉')
elif omikuji <= 7: #5,6,7
    print('凶')
else:               #5,6,7
    print('大凶')


# datetimeで現在日時を取得
import datetime
seireki = datetime.date.today().year
print('西暦'+str(seireki)+'年は、',end="")

heisei = seireki - 1988
print('平成'+str(heisei)+'年です。')


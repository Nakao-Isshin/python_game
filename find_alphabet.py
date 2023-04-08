import random
import datetime
ALP = [chr(i) for i in range(ord("A"), ord("A")+26)]

r = random.choice(ALP)
alp = ""
for i in ALP:
    if i != r:
        alp = alp + i
print(alp)
st = datetime.datetime.now()
ans = input("抜けているアルファベットは？")
if ans == r:
    print("正解です")
    et = datetime.datetime.now()
    print(f"{(et - st).seconds}秒かかりました")
else:
    print("違います")
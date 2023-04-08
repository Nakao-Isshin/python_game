import random
pl_pos = 1
com_pos = 1


def banmen():
    print("・"*(pl_pos-1) + "P" + "・"*(30-pl_pos) + "Goal")
    print("・"*(com_pos-1) + "P" + "・"*(30-com_pos) + "Goal")


while True:
    banmen()
    input("ENTERを押すとあなたのコマが進みます")
    pl_pos += random.randint(1, 6)
    if pl_pos > 30:
        pl_pos = 30
    banmen()
    if pl_pos == 30:
        print("あなたの勝ちです")
        break
    input("ENTERを押すとコンピュータのコマが進みます")
    com_pos += random.randint(1, 6)
    if com_pos > 30:
        com_pos = 30
    banmen()
    if com_pos == 30:
        print("コンピュータの勝ちです")
        break

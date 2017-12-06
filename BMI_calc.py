# -*- coding: utf-8 -*-

#BMI 计算

while True:
    weight = input('请输入您的体重（KG）如需退出，请输入“退出”：')
    if weight == '退出':
        exit()
    else:
        weight = int(weight)
    height = float(input('请输入您的身高（M）：'))

    BMI = weight / (height**2)

    if BMI < 18.5:
        print('您太廋了，要多吃点东西哦~~')
    elif 18.5 <= BMI < 25:
        print('太棒了，您的身体真好！')
    elif 25 <= BMI < 30:
        print('嗨呀，您的身体稍微好了一点点，要多做运动哦~~')
    else:
        print('哼！您真是太胖了呢！！一定要少吃东西多运动哦~~')

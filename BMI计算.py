# 这是一个算BMI的小程序。
# -*- coding: utf-8 -*-
import math
height =float(input('请输入身高：'))
weight =float(input('请输入体重：'))
BMI = weight / (height**2)
if BMI < 18.5:
    print('过轻')
elif 18.5 < BMI < 25:
    print('正常')
elif 28 < BMI < 32:
    print('过重')
else:
    print('严重肥胖')

from numpy import *

# 引入矩阵模块
# 打印一个随机数组
random.rand(4, 4)  # 在numpy中存在array和matrix两种数据类型
# 调用mat()方法将数组转化为矩阵
randMat = mat(random.rand(4, 4))
print(type(randMat))
print(randMat)
# 求矩阵的逆
invRandMat = randMat.I
print(randMat.I)
# 矩阵和自己的逆相乘
print(randMat * invRandMat)
# 创建单位阵
myEye=eye(4,4)
print(randMat * invRandMat-myEye)
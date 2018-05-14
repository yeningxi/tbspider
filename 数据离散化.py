import numpy
import pandas as pds

# 读取数据
data = pds.read_excel('selenium教程.xls')

# 数据横排
data2 = data.T
# 取出要处理的行（价格）
data3 = data2.values[4]
# cut做数据离散型处理
data4 = pds.cut(data3,[0,100,300,500,800,data3.max()],labels=['很便宜','便宜','适中','贵','很贵'])


def main():
    print(data4)

if __name__ == '__main__':
    main()




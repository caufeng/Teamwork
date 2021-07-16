# -*- coding: gbk -*-#防止代码编码报错
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

def wyy():#可视化网易云10位热门歌手的评论数分布图
    sum1=0
    x = ('薛之谦', '林俊杰', '陈奕迅', '刘大壮', '颜人中', '毛不易', 'JBiebs', '大籽', '许嵩', 'Lil E')#10位歌手
    y = np.arange(10)
    for i in range(10):#分别读取评论文件
        filename = '网易云评论' + str(i + 1) + '.csv'
        data = pd.read_csv(filename, header=None, skiprows=1, encoding='gb2312')
        data[1] = data[1].str.replace('条', '')
        data[1] = data[1].astype(int)#改变数据类型，方便计数
        y[i] = data[1].sum()
        sum1=sum1+y[i]#求网易云平台总评数
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
    params = {'figure.figsize': '10, 5'}#设置画布 画图
    plt.rcParams.update(params)
    plt.grid(linestyle="-.", axis='y', alpha=0.4)
    plt.bar(x, y, color=['b', 'g', 'r', 'c', 'm', 'm', 'c', 'r', 'g', 'b'])
    plt.xlabel('歌手')
    plt.ylabel('评论数')
    plt.title('网易云音乐10大热门歌手评论数')
    for a, b in zip(x, y):#显示数据
        plt.text(a, b - 0.3, b, ha='center', va='bottom', fontsize=10)
    plt.savefig('网易云音乐10大热门歌手评论分布图.png')
    plt.show()
    return sum1
def qq():#可视化QQ音乐10位热门歌手的评论数分布图
    sum2=0
    x = ('周杰伦', '七叔', '王靖雯不胖', '不是花火呀', '薛之谦', '林俊杰', '任然', '海来阿木', '姚六一', '郑鱼')
    y = np.arange(10)
    for i in range(10):
        filename = 'QQmusic' + str(i + 1) + '.csv'
        data = pd.read_csv(filename, header=None)
        y[i] = data[1].sum()
        sum2=sum2+y[i]
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
    params = {'figure.figsize': '10, 5'}
    plt.rcParams.update(params)
    plt.grid(linestyle="-.", axis='y', alpha=0.4)
    plt.bar(x, y, color=['b', 'g', 'r', 'c', 'm', 'm', 'c', 'r', 'g', 'b'])
    plt.xlabel('歌手')
    plt.ylabel('评论数')
    plt.title('QQ音乐10大热门歌手评论数')
    for a, b in zip(x, y):
        plt.text(a, b - 0.3, b, ha='center', va='bottom', fontsize=10)
    plt.savefig('QQ音乐10大热门歌手评论分布图.png')
    plt.show()
    return sum2
def comments_compare():#绘制两个平台评论数的饼状图，作对比
    sum1=wyy()
    sum2=qq()
    sum=sum1+sum2
    sum1=round(sum1*100/sum,2)
    sum2=round(sum2*100/sum,2)
    x=[sum1,sum2]
    label=['网易云热门歌手评论数','QQ音乐热门歌手评论数']
    plt.pie(x,labels=label,shadow=True,autopct='%1.1f%%',)
    plt.title('QQ音乐和网易云音乐热门歌手评论数对比图')
    plt.savefig('两平台热门歌手评论数对比图.png')
    plt.show()
def main():
    comments_compare()
main()
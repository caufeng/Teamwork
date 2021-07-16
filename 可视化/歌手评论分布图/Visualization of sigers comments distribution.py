# -*- coding: gbk -*-#防止代码编码报错
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

def wyy():#可视化网易云10位热门歌手的评论分布图
    name = ('薛之谦', '林俊杰', '陈奕迅', '刘大壮', '颜人中', '毛不易', 'JBiebs', '大籽', '许嵩', 'Lil E')  # 10位歌手
    y = np.arange(10)
    for i in range(10):
        filename = '网易云评论' + str(i + 1) + '.csv'
        data = pd.read_csv(filename, header=None, skiprows=1, encoding='gb2312')
        x=data[0]
        data[1] = data[1].str.replace('条', '')
        data[1] = data[1].astype(int)#改变数据类型，方便计数
        y=data[1]
        plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
        params = {'figure.figsize': '10, 5'}#设置画布 画图
        plt.rcParams.update(params)
        plt.grid(linestyle="-.", axis='y', alpha=0.4)
        plt.bar(x, y, color=['b', 'g', 'r', 'c', 'm', 'm', 'c', 'r', 'g', 'b'])
        plt.xticks(x, x, rotation=15)
        plt.ylabel('评论数')
        title='网易云'+str(name[i])+'评论分布图'
        plt.title(title)
        for a, b in zip(x, y):#显示数据
            plt.text(a, b - 0.3, b, ha='center', va='bottom', fontsize=10)
        filename='网易云'+str(name[i])+'评论分布图.png'
        plt.savefig(filename)
        plt.show()
def QQ():#可视化QQ音乐10位热门歌手的评论分布图
    name = ('周杰伦', '七叔', '王靖雯不胖', '不是花火呀', '薛之谦', '林俊杰', '任然', '海来阿木', '姚六一', '郑鱼')  # 10位歌手
    y = np.arange(10)
    for i in range(10):
        filename = '网易云评论' + str(i + 1) + '.csv'
        data = pd.read_csv(filename, header=None, skiprows=1, encoding='gb2312')
        x=data[0]
        data[1] = data[1].str.replace('条', '')
        data[1] = data[1].astype(int)
        y=data[1]
        plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
        params = {'figure.figsize': '10, 5'}
        plt.rcParams.update(params)
        plt.grid(linestyle="-.", axis='y', alpha=0.4)
        plt.bar(x, y, color=['b', 'g', 'r', 'c', 'm', 'm', 'c', 'r', 'g', 'b'])
        plt.xticks(x, x, rotation=15)
        plt.ylabel('评论数')
        title='QQ音乐'+str(name[i])+'评论分布图'
        plt.title(title)
        for a, b in zip(x, y):
            plt.text(a, b - 0.3, b, ha='center', va='bottom', fontsize=10)
        filename='QQ音乐'+str(name[i])+'评论分布图.png'
        plt.savefig(filename)
        plt.show()
wyy()
QQ()


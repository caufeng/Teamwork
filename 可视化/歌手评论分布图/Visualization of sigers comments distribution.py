# -*- coding: gbk -*-#��ֹ������뱨��
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

def wyy():#���ӻ�������10λ���Ÿ��ֵ����۷ֲ�ͼ
    name = ('Ѧ֮ǫ', '�ֿ���', '����Ѹ', '����׳', '������', 'ë����', 'JBiebs', '����', '����', 'Lil E')  # 10λ����
    y = np.arange(10)
    for i in range(10):
        filename = '����������' + str(i + 1) + '.csv'
        data = pd.read_csv(filename, header=None, skiprows=1, encoding='gb2312')
        x=data[0]
        data[1] = data[1].str.replace('��', '')
        data[1] = data[1].astype(int)#�ı��������ͣ��������
        y=data[1]
        plt.rcParams['font.sans-serif'] = 'SimHei'  # ����������ʾ
        params = {'figure.figsize': '10, 5'}#���û��� ��ͼ
        plt.rcParams.update(params)
        plt.grid(linestyle="-.", axis='y', alpha=0.4)
        plt.bar(x, y, color=['b', 'g', 'r', 'c', 'm', 'm', 'c', 'r', 'g', 'b'])
        plt.xticks(x, x, rotation=15)
        plt.ylabel('������')
        title='������'+str(name[i])+'���۷ֲ�ͼ'
        plt.title(title)
        for a, b in zip(x, y):#��ʾ����
            plt.text(a, b - 0.3, b, ha='center', va='bottom', fontsize=10)
        filename='������'+str(name[i])+'���۷ֲ�ͼ.png'
        plt.savefig(filename)
        plt.show()
def QQ():#���ӻ�QQ����10λ���Ÿ��ֵ����۷ֲ�ͼ
    name = ('�ܽ���', '����', '����������', '���ǻ���ѽ', 'Ѧ֮ǫ', '�ֿ���', '��Ȼ', '������ľ', 'Ҧ��һ', '֣��')  # 10λ����
    y = np.arange(10)
    for i in range(10):
        filename = '����������' + str(i + 1) + '.csv'
        data = pd.read_csv(filename, header=None, skiprows=1, encoding='gb2312')
        x=data[0]
        data[1] = data[1].str.replace('��', '')
        data[1] = data[1].astype(int)
        y=data[1]
        plt.rcParams['font.sans-serif'] = 'SimHei'  # ����������ʾ
        params = {'figure.figsize': '10, 5'}
        plt.rcParams.update(params)
        plt.grid(linestyle="-.", axis='y', alpha=0.4)
        plt.bar(x, y, color=['b', 'g', 'r', 'c', 'm', 'm', 'c', 'r', 'g', 'b'])
        plt.xticks(x, x, rotation=15)
        plt.ylabel('������')
        title='QQ����'+str(name[i])+'���۷ֲ�ͼ'
        plt.title(title)
        for a, b in zip(x, y):
            plt.text(a, b - 0.3, b, ha='center', va='bottom', fontsize=10)
        filename='QQ����'+str(name[i])+'���۷ֲ�ͼ.png'
        plt.savefig(filename)
        plt.show()
wyy()
QQ()


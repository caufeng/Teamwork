# -*- coding: gbk -*-#��ֹ������뱨��
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

def wyy():#���ӻ�������10λ���Ÿ��ֵ��������ֲ�ͼ
    sum1=0
    x = ('Ѧ֮ǫ', '�ֿ���', '����Ѹ', '����׳', '������', 'ë����', 'JBiebs', '����', '����', 'Lil E')#10λ����
    y = np.arange(10)
    for i in range(10):#�ֱ��ȡ�����ļ�
        filename = '����������' + str(i + 1) + '.csv'
        data = pd.read_csv(filename, header=None, skiprows=1, encoding='gb2312')
        data[1] = data[1].str.replace('��', '')
        data[1] = data[1].astype(int)#�ı��������ͣ��������
        y[i] = data[1].sum()
        sum1=sum1+y[i]#��������ƽ̨������
    plt.rcParams['font.sans-serif'] = 'SimHei'  # ����������ʾ
    params = {'figure.figsize': '10, 5'}#���û��� ��ͼ
    plt.rcParams.update(params)
    plt.grid(linestyle="-.", axis='y', alpha=0.4)
    plt.bar(x, y, color=['b', 'g', 'r', 'c', 'm', 'm', 'c', 'r', 'g', 'b'])
    plt.xlabel('����')
    plt.ylabel('������')
    plt.title('����������10�����Ÿ���������')
    for a, b in zip(x, y):#��ʾ����
        plt.text(a, b - 0.3, b, ha='center', va='bottom', fontsize=10)
    plt.savefig('����������10�����Ÿ������۷ֲ�ͼ.png')
    plt.show()
    return sum1
def qq():#���ӻ�QQ����10λ���Ÿ��ֵ��������ֲ�ͼ
    sum2=0
    x = ('�ܽ���', '����', '����������', '���ǻ���ѽ', 'Ѧ֮ǫ', '�ֿ���', '��Ȼ', '������ľ', 'Ҧ��һ', '֣��')
    y = np.arange(10)
    for i in range(10):
        filename = 'QQmusic' + str(i + 1) + '.csv'
        data = pd.read_csv(filename, header=None)
        y[i] = data[1].sum()
        sum2=sum2+y[i]
    plt.rcParams['font.sans-serif'] = 'SimHei'  # ����������ʾ
    params = {'figure.figsize': '10, 5'}
    plt.rcParams.update(params)
    plt.grid(linestyle="-.", axis='y', alpha=0.4)
    plt.bar(x, y, color=['b', 'g', 'r', 'c', 'm', 'm', 'c', 'r', 'g', 'b'])
    plt.xlabel('����')
    plt.ylabel('������')
    plt.title('QQ����10�����Ÿ���������')
    for a, b in zip(x, y):
        plt.text(a, b - 0.3, b, ha='center', va='bottom', fontsize=10)
    plt.savefig('QQ����10�����Ÿ������۷ֲ�ͼ.png')
    plt.show()
    return sum2
def comments_compare():#��������ƽ̨�������ı�״ͼ�����Ա�
    sum1=wyy()
    sum2=qq()
    sum=sum1+sum2
    sum1=round(sum1*100/sum,2)
    sum2=round(sum2*100/sum,2)
    x=[sum1,sum2]
    label=['���������Ÿ���������','QQ�������Ÿ���������']
    plt.pie(x,labels=label,shadow=True,autopct='%1.1f%%',)
    plt.title('QQ���ֺ��������������Ÿ����������Ա�ͼ')
    plt.savefig('��ƽ̨���Ÿ����������Ա�ͼ.png')
    plt.show()
def main():
    comments_compare()
main()
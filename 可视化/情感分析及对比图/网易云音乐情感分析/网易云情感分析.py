from snownlp import SnowNLP
import matplotlib.pyplot as plt
import numpy as np

def snowanalysis(self,j):
    sentimentslist = [] #创建列表来保存情感分析的结果
    for li in self:
        try:
 #           print(li)
            s = SnowNLP(li)  #用SnowNLP进行情感分析
  #          print(s.sentiments)
            sentimentslist.append(s.sentiments)  #并将结果添加到列表中
        except:
            continue
    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01)) #画出情感分析图
    plt.xlabel("The comments distribution")
    plt.savefig('分布图'+str(j)+'.jpg')
    # plt.show()
    plt.close()
 #   print(sentimentslist)

    for i in range(len(sentimentslist)):  #将情感分析所得结果归为积极的和消极的两类
        if (sentimentslist[i] > 0.5):     #大于0.5为积极的情感，小于0.5为消极的情感
            sentimentslist[i] = 1
        else:
            sentimentslist[i] = -1
 #  print(sentimentslist)
    info = []
    a = 0
    b = 0
    for x in range(0, len(sentimentslist)): #将所分好的两大类情感进行可视化
        if (sentimentslist[x] == 1): #分别计算两类情感的数量
            a = a + 1
        else:
            b = b + 1
    info.append(b)  #将其添加到info列表中
    info.append(a)
    print(info)
    info2 = ['negative', 'positive']
    plt.bar(info2, info, tick_label=info2, color='#2FC25B') #用柱状图进行可视化
    plt.xlabel("comments analyst")
    plt.savefig('评论积极消极分析图'+str(j)+'.jpg')
    # plt.show()
    plt.close()
    info.remove(a) #移除数据，为进行下一次评论的分析做准备
    info.remove(b)

for i in range(1,11):
    comment = []  #创建列表
    csvname="comment\comment_csv"+str(i)+".csv"  #输入文件名
    with open(csvname, mode='r', encoding='utf-8') as f:  #打开文件
        rows = f.readlines()  #读取文件中的每一行
  #      print(rows)
        for row in rows:
            if row not in comment:
                comment.append(row.strip('\n')) #将文件中的每一行评论添加到comment列表中
 #       print(comment)
    snowanalysis(comment,i)  #进行情感分析
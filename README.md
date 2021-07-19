# Teamwork
## 项目内容
我们的项目方向为爬取网易云和QQ音乐较火的歌单（查询2020年网易云和QQ音乐年度10大单曲）中歌曲的评论（五千条以上），根据评论可视化分析（词云图，情感分析），然后进行两个平台的对比。
此外，我们还将爬取两个音乐平台上较火的十位歌手（每位歌手选取了10首较火的代表作），爬取他们的歌曲评论数等数据，进行可视化分析，进行对比。  
最后的成果以网页的形式展示。  
QQ音乐2020十大单曲：《Mojito》《后来遇见他》《天外来物》《How You Like That》《不爱我》《飞鸟和蝉》《情人》《起风了》《会好的》《Maria（마리아）》  
网易云2020十大单曲：《天外来物》《会不会（吉他版）》《经济舱》《夏天的风》《海底》《丢了你》《大眠（完整版）》《他只是经过》《与我无关》《好像爱这个世界啊》  
QQ音乐热门歌手：周杰伦 七叔 王靖雯不胖 不是花火呀 薛之谦 林俊杰 任然 海来阿木 姚六一 郑鱼  
网易云热门歌手：薛之谦 林俊杰 陈奕迅 刘大壮 颜人中 毛不易 JBiebs 大籽 许嵩 Lil E  
![image](https://github.com/caufeng/Teamwork/raw/master/images/qq.png)  
![image](https://github.com/caufeng/Teamwork/raw/master/images/wyy.png) 
## 成员分工
冯一凡和韦昌晖分别负责歌曲、歌手的数据爬取、可视化，刘志昊、尹攀、武山富负责网页制作
## 项目开展过程
7.12 立项  
7.13-7.16 爬取数据并做可视化  
7.15-7.19 将可视化数据制作成网页  
## 项目特色介绍
### 爬虫介绍
1.在爬取歌曲、歌手评论时基本采用selenium库爬取（特别是爬取歌曲评论），因为：  
#### QQ音乐和网易云音乐都是大厂，网站具有一定的反爬能力  
#### 爬取歌曲评论，我们每首歌都爬取了六七千条，需要翻页数百次，没有selenium的自动爬取功能，将是巨大的工作量。  
2.我们在爬虫代码中，将各功能（爬取、保存、词语图）封装函数，并加以注释，简洁明了。同时，我们将爬取的歌曲（歌手）以列表形式开展，大大减少了代码量（但是代码工作时间的优化存在一定问题）；  
3.在爬取歌曲评论部分，我们省略了歌曲评论的时间、评论用户名、点赞数等无关数据，一来这些数据会影响代码爬取效率，二来数据对我们的项目无太大帮助，三来词云图及情感分析可能会受这些数据影响；  
### 可视化介绍  
1.在可视化代码中，我们尽量挖掘爬取数据中可用的信息，并想在两个平台做出对比（词云图、情感指数、评论数）；  
2.基于项目主题，我们做了20首单曲评论的词云图、情感分析，可以从中看出一些差别；  
2.基于项目主题，我们做了两个平台歌手评论的分布，看看谁是平台评论的“顶流”，并且我们做了两个平台热门歌手评论数的一个对比，看看那个平台用户更爱留下评论。我们还做了20位热门歌手的10首歌的评论分布图，看看哪些歌手是一炮而红。  
### 网页介绍  

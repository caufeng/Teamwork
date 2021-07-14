from selenium import webdriver
import pandas as pd
import csv  # 数据保存
import jieba  # 分词处理
import numpy  # 图片的转换
from PIL import Image  # 图片处理
from wordcloud import WordCloud  # 词云制作
from time import sleep #设置睡眠时间

def get_comment_csv(x,m):
    driver = webdriver.Firefox()
    url = 'https://music.163.com/#/song?id='+x  # 歌曲页面的URL地址
    driver.get(url)
    driver.implicitly_wait(30)  # 显式等待10秒
    driver.switch_to.frame('contentFrame')  # 切入contentFrame
    comments_list = []
    for i in range(300):  # 爬取评论的页数
        next_button = driver.find_element_by_xpath('//*[@class="m-cmmt"]/div[3]/div/a[11]')  # 找到下一页的按钮
        comments = driver.find_elements_by_xpath('//*[@class="m-cmmt"]/div[2]/div/div[2]/div[1]/div')  # 找到评论
        for item in comments:
            index = item.text.index('：') + 1
            comment = item.text[index:]  # 解析评论
            comments_list.append(comment)
            df = pd.DataFrame({'评论内容':comments_list})
            filename='comment_csv'+str(m)+'.csv'
            df.to_csv(filename, encoding='utf-8', index=False)
        driver.execute_script("arguments[0].click();", next_button)  # 触发next_button的JS进入下一页评论
    driver.close()
    return filename
def make_world_cloud(filename,i):
    with open(filename, encoding='utf-8') as f:
        comment_text = f.read()
    # 去除没有意义的停用词，停用词在stopwords.txt文件中保存
    excludes = open(file='C:\\Users\\lenovo\\Desktop\\stopwords.txt', encoding='utf-8').read().splitlines()
    for j in excludes:
        comment_text = comment_text.replace(j, '')
    comment_text1 = comment_text.replace(' ', '')
    print('successfully delete')
    # 利用jieba库进行分词处理,需要将歌名加入词库
    jieba.load_userdict('C:\\Users\\lenovo\\Desktop\\song and singer name of wangyiyun.txt')
    comment_cut = jieba.cut(comment_text)#使用cut函数进行分词
    comment_text = ''.join(comment_cut)
    print('successfully separate')
    # 打开图片并转换为数组形式
    imagename = 'C:\\Users\\lenovo\\Desktop\\wbg\\bg' + str(i) + '.png'
    photo = numpy.array(Image.open(imagename))
    # 指定字体、背景颜色、宽高、词量、指定的背景图
    wc = WordCloud(font_path='C:/Windows/Fonts/simsun.ttc', background_color="white", width=1200, height=900,
                   max_words=400, mask=photo)
    # 生成词云
    wc.generate(comment_text)
    # 展示词云
    image_produce = wc.to_image()
    image_produce.show()
    # 保存到本地
    savename = 'worldcloud' + str(i) + '.png'
    wc.to_file(savename)
    print('world_cloud image successfully save')
def main():
    x = ['1463165983', '1481164987', '1487528112', '1436709403', '1430583016', '1442508316', '1413142894', '1443838552',
         '1413585838', '1436910205']
    for i in range(10):
        filename = get_comment_csv(x[i], i + 1)
        make_world_cloud(filename,i+1)
main()



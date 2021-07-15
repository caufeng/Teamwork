from selenium import webdriver
import csv
from time import sleep
import time
import jieba  # 分词处理
import numpy  # 图片的转换
from PIL import Image  # 图片处理
from wordcloud import WordCloud  # 词云制作

def getSongResourse(url):
    # 创建Chrome浏览器对象
    driver = webdriver.Firefox()
    song_resourse={}
    driver.get(url)
    # 这2秒用于等待页面所有异步请求的完成
    sleep(2)
    # 获取评论
    comments=[]
    # # 点击加载更多，每次多出25条评论
    for i in range(300):
         try:
             # 评论
             comments_list = driver.find_element_by_css_selector(".js_all_list").find_elements_by_tag_name("li")
             for com in comments_list:
                 # 内容
                 content = com.find_element_by_css_selector(".js_hot_text").text
                 # 创建一个空的comment字典
                 comment = {}
                 # 更新内容、时间、点赞数
                 comment.update({"评论内容": content})
                 # 将每一条comment存入总的comments中
                 comments.append(comment)
             driver.implicitly_wait(10)
             button=driver.find_element_by_class_name('next')
             button.click()
         except:
             sleep(0.5)
    sleep(0.5)
    song_resourse.update({"评论":comments})
    return song_resourse


def savefile(urlist, k):
    song_resourses = []
    # 打开QQ音乐
    url = 'https://y.qq.com/n/yqq/song/' + urlist[k] + '.html'
    driver.get("https://y.qq.com/n/yqq/song/" + urlist[k] + ".html")
    # csv文件配置
    filename = 'comment csv' + str(k+1) + '.csv'
    csv_file = open(filename, 'w', newline='', encoding='utf-8-sig')
    writer = csv.writer(csv_file)
    song_resourses.append(getSongResourse(url))
    for i in song_resourses:
        for j in i["评论"]:
            writer.writerow([j["评论内容"]])
    csv_file.close()
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
    # 利用jieba库进行分词处理,需要将歌名及歌手加入词库
    jieba.load_userdict('C:\\Users\\lenovo\\Desktop\\song and singer name of wangyiyun.txt')
    comment_cut = jieba.cut(comment_text)#使用cut函数进行分词
    comment_text = ''.join(comment_cut)
    print('successfully separate')
    # 打开图片并转换为数组形式
    imagename = 'C:\\Users\\lenovo\\Desktop\\qbg\\bg' + str(i) + '.png'
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
    savename = 'qqworldcloud' + str(i) + '.png'
    wc.to_file(savename)
    print('world_cloud image successfully save')
def main():
    urlist = ['001glaI72k8BQX', '000OjsEW0QrPAd',
              '0013WPvt4fQH2b', '0026GG814HkHcw',
              '0013KFa32c9lVn', '004Fimy419PpsA',
              '000aWBBQ2fMyBJ', '002w57E00BGzXn',
              '001rujaV3AzLqt', '000rxu503rIonP']
    for i in range(10):
        filename=savefile(urlist,i)
        make_world_cloud(filename,i+1)
main()







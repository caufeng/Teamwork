from selenium import webdriver
import csv
from time import sleep
import time

# 获取一首歌曲所需要的信息
def getSongResourse(url):
    song_resourse={}
    driver.get(url)
    # 这2秒用于等待页面所有异步请求的完成
    sleep(2)

    # 获取歌曲名
    song_name=driver.find_element_by_class_name("data__name_txt").text
    # 获取流派，发行时间，评论数
    song_comment_num = driver.find_element_by_css_selector(".js_into_comment").text[3:-1]

    song_resourse.update({"歌曲名":song_name})
    song_resourse.update({"评论数":song_comment_num})
    return song_resourse

#创建Chrome浏览器对象
driver=webdriver.Chrome()
#打开QQ音乐
urllist = ['0025NhlN2yWrP4','004gGNH91beMrM','002YetSZ06c9c9','003LABmP0dTIWp','002J4UUk29y8BY',
'001BLpXF2DyJe2','00067r4p0wBDDN','004WYT5j1s7R6Y','000P8v78226j0Y','000RAXlq3QVMrT']
for i in range(10):
    driver.get("https://y.qq.com/n/yqq/singer/"+urllist[i]+".html")
    #csv文件配置
    csv_file = open('QQ评论'+str(i)+'.csv','w',newline='',encoding='utf-8-sig')
    writer = csv.writer(csv_file)
    # 取前十首歌曲
    song_numer=10
    # #前十首歌曲url列表
    song_url_list=[]
    # #前十首歌曲所需要的信息
    song_resourses=[]
    #使用selenium找到songlist__item
    songlist__item=driver.find_elements_by_class_name("songlist__item")
    # 获取所有歌曲url
    for song in songlist__item:
        song__url=song.find_element_by_class_name("js_song").get_attribute("href")
        song_url_list.append(song__url)
        song_numer-=1
        if(song_numer==0):
            break
    for song_page in song_url_list:
        song_resourses.append(getSongResourse(song_page))
    for i in song_resourses:
        writer.writerow([i["歌曲名"],i["评论数"]])
    csv_file.close()